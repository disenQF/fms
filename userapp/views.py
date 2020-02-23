import os

from django.core.files.uploadedfile import UploadedFile
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from common import files_stack, alisms_, file_mime_
from fms import settings
from .models import TUser, TFile, TImageLinks


def send_code(request):
    phone = request.GET.get('phone', '')
    if phone:
        code = cache_.new_code(phone)  # 生成新的code
        # 发送验证码短信
        alisms_.send_code(phone, code)
        return JsonResponse({
            'state': 0,
            'msg': '发送成功'
        })

    return JsonResponse({
        'state': 1,
        'msg': '发送失败，请输入正确的手机号'
    })


class RegistView(View):
    def get(self, request):
        return render(request, 'regist.html')

    def post(self, request):
        phone = request.POST.get('phone', '')
        code = request.POST.get('code', '')
        password = request.POST.get('password')

        if not all((phone, code, password)):
            error = '注册失败,必须输入手机号、验证码和口令!'
        else:
            # 判断输入的验证码是否为向手机端发送的验证码
            if cache_.get_code(phone) != code:
                error = '请输入正确的验证码'
            else:
                user = TUser(phone=phone, auth_string=password)
                user.save()

                request.session['login_user'] = {
                    '_id': user.user_id,
                    'name': user.phone,
                    'code': ''  # 角色的code，不设置但必须是空字符串
                }

                return redirect('/')

        return render(request, 'regist.html', locals())


class FileView(View):
    def get(self, request):
        current_file_id = int(request.GET.get('current_file_id', 0))
        current_file_name = request.GET.get('current_file_name', '根')

        if current_file_id == 0:
            files_stack.clear_pre_file_stack()

        files_stack.add_file_stack(current_file_id, current_file_name)

        pre_file_stack = files_stack.get_pre_file_stack()
        files = TFile.objects.filter(parent_file_id=current_file_id)
        return render(request, 'files/list.html', locals())

    def update_file_path(self, file_id, old_file_path, new_file_path):
        files = TFile.objects.filter(parent_file_id=file_id)

        for file_obj in files.all():
            file_obj.file_path = file_obj.file_path.replace(old_file_path, new_file_path)
            file_obj.save()

            self.update_file_path(file_obj.file_id, old_file_path, new_file_path)

    def post(self, request):
        print(request.POST)

        current_file_id = int(request.POST.get('current_file_id', 0))
        current_file_name = request.POST.get('current_file_name', '')

        user_id = request.session['login_user']['_id']  # 当前会话的用户ID

        action = request.POST.get('action', '')
        if action and action == 'new_dir':
            # user = TUser.objects.get(pk=request.session['login_user']['_id'])

            dir_path = settings.SAVE_ROOT_PATH + f"-{user_id}" + (
                "/" + current_file_name if current_file_name != '根' else '')

            file_name = request.POST.get('dir_name')
            file_path = os.path.join(dir_path, file_name)

            file = TFile(file_name=file_name,
                         file_path=file_path,
                         parent_file_id=current_file_id,
                         user_id=user_id)
            file.save()
            os.makedirs(file_path)  # 服务器创建目录

        if action and action == 'del':
            # 删除这个文件下的所有子目录和文件
            TFile.objects.filter(parent_file_id=request.POST.get('file_id')).delete()
            file = TFile.objects.get(pk=request.POST.get('file_id'))
            # 服务器的删除文件操作
            os.system(f'rm -rf {os.path.join(file.file_path)}')

            file.delete()

        if action and action == 'rename':
            file = TFile.objects.get(pk=request.POST.get('file_id'))
            file.file_name = request.POST.get('dir_name', '')

            old_file_path = file.file_path  # 原目录
            dir_path, _ = os.path.split(file.file_path)
            new_file_path = os.path.join(dir_path, file.file_name)

            os.system(f'mv {file.file_path} {new_file_path}')  # 执行服务器的修改文件目录名命令

            file.file_path = new_file_path  # 更新数据库的新文件路径
            file.save()

            if file.file_type == 0:
                # 查询所有的子级目录
                self.update_file_path(file.file_id, old_file_path, new_file_path)

        if action and action == 'prefiles':
            current_file_id, current_file_name = files_stack.pop_file_stack()

        if action and action == 'upload':
            print('文件上传')

            upload_file: UploadedFile = request.FILES.get('file')
            # 判断当前目录是否为根路径
            if not current_file_id:
                save_dir = settings.SAVE_ROOT_PATH + f'-{user_id}'
                os.makedirs(save_dir)
            else:
                save_dir = TFile.objects.get(pk=current_file_id).file_path

            save_file_path = os.path.join(save_dir, upload_file.name)

            TFile.objects.create(file_name=upload_file.name,
                                 file_type=file_mime_.get_file_type(upload_file.content_type),
                                 file_path=save_file_path,
                                 user_id=user_id,
                                 file_size=upload_file.size,
                                 parent_file_id=current_file_id)

            with open(save_file_path, 'wb') as f:
                for chunk in upload_file.chunks():
                    f.write(chunk)

        return JsonResponse({
            'url': '/user/files/?current_file_id=' + str(current_file_id) + "&current_file_name=" + current_file_name
        })


def download(request):
    # 下载文件
    from urllib.parse import quote

    file_id = request.GET.get('file_id')
    file = TFile.objects.get(pk=file_id)
    with open(file.file_path, 'rb') as f:
        bytes = f.read()

    resp = HttpResponse(content=bytes, content_type='application/octet-stream', charset='utf-8')
    resp.setdefault('Content-Disposition', 'attachment;filename=' + quote(file.file_name, encoding='utf-8'))
    resp.setdefault('Content-Length', file.file_size)

    return resp


def show_img(request):
    file_id = request.GET.get('file_id')
    file = TFile.objects.get(pk=file_id)
    with open(file.file_path, 'rb') as f:
        bytes = f.read()

    return HttpResponse(content=bytes, content_type='image/*', charset='utf-8')


def create_image_link(request):
    file_id = request.GET.get('file_id')

    return render(request, 'files/edit.html',locals())
