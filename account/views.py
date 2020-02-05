# Create your views here.
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    if request.method == "POST":  # POST请求方式时验证表单提交用户名密码
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return HttpResponse("Wellcome You. You hava been authenticate successfully")
            else:
                return HttpResponse("Sorry. Your username or password is not right.")
        else:
            return HttpResponse("Invalid login")

    if request.method == "GET":  # GET请求方式时，返回登录页面
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})
