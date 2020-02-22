from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from common import cache_, alisms_
from .models import TUser


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
                    'code': '' # 角色的code，不设置但必须是空字符串
                }

                return redirect('/')

        return render(request, 'regist.html', locals())


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
