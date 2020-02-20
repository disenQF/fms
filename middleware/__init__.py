#!/usr/bin/python3
# coding: utf-8
from django.http import HttpRequest
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class LoginMiddleware(MiddlewareMixin):

    no_filter_path = (
        '/login/',
        '/logout/'
        '/regist/'
    )

    def process_request(self, request: HttpRequest):
        if request.path not in self.no_filter_path:
            # 验证当前会话是否已登录
            if not request.session.get('login_user', None):
                return redirect('/login/')


