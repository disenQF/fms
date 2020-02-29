#!/usr/bin/python3
# coding: utf-8
from django.http import HttpRequest
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class LoginMiddleware(MiddlewareMixin):

    no_filter_path = (
        '/login/',
        '/logout/',
        '/user/regist/',
        '/user/code/'
    )

    def process_request(self, request: HttpRequest):
        if any((request.path not in self.no_filter_path,
                not request.path.startswith('/s/'),
                not request.path.startswith('/m/'))):
            # 验证当前会话是否已登录
            if not request.session.get('login_user', None):
                return redirect('/login/')


