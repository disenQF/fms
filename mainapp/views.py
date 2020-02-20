from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'dashboard.html')


def role(request):
    from .models import TSysRole
    roles = TSysRole.objects.all()
    return render(request, 'role.html', locals())