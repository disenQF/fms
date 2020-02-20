from django.shortcuts import render, redirect

from common import md5_
from .models import TSysUser
from .models import TUser

# Create your views here.
def login(request):
    # 分两种用户，一个是会员，一个管理员（系统）
    print('--->', request.method)
    if request.method == 'POST':
        print(request.POST)

        error = None

        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        remeber = request.POST.get('remeber', '')  # checkbox

        password_ = md5_.hash_encode(password)  # 转成md5后的密文

        # 验证用户名和口令是否为空
        if not all((username, password)):
            error = f'用户名或口令不能为空！'

        login_user = TSysUser.objects.filter(username=username, auth_string=password_).first()
        if login_user:
            # 系统管理员
            role_ = login_user.role
            login_info = {
                '_id': login_user.id,
                'name': role_.name,
                'code': role_.code
            }

        else:
            login_user = TUser.objects.filter(name=username, auth_string=password).first()
            if login_user:
                # 会员
                login_info = {
                    '_id': login_user.user_id,
                    'name': login_user.name,
                    'code': '',
                    'head': login_user.head,
                    'email': login_user.mail,
                    'phone': login_user.phone
                }
            else:
                error = f'{username} 用户名或口令错误！'

        if not error:
            request.session['login_user'] = login_info
            return redirect('/')

    return render(request, 'login.html', locals())


def logout(request):
    del request.session['login_user']
    return redirect('/login/')

def index(request):
    return render(request, 'dashboard.html')


def role(request):
    from .models import TSysRole
    roles = TSysRole.objects.all()
    return render(request, 'role.html', locals())