#!/usr/bin/python3
# coding: utf-8

from django import forms
from .models import TSysRole, TSysUser, TMessage


class RoleForm(forms.ModelForm):

    class Meta:
        model = TSysRole
        fields = ['name', 'code']  # '__all__'
        error_messages = {
            'name': {
                'required': '角色名不能为空'
            },
            'code': {
                'required': '角色代码不能为空'
            }
        }

class SysUserForm(forms.ModelForm):

    class Meta:
        model = TSysUser
        fields = ['username', 'auth_string', 'role_id', 'nick_name']  # '__all__'
        error_messages = {
            'username': {
                'required': '账号不能为空'
            },
            'auth_string': {
                'required': '口令不能为空'
            },
            'role_id': {
                'required': '系统用户角色不能为空'
            }
        }


class MessageForm(forms.ModelForm):

    class Meta:
        model = TMessage
        fields = ['title', 'content', 'link_url', 'create_time']  # '__all__'
        error_messages = {
            'title': {
                'required': '标题不能为空'
            },
            'link_url': {
                'required': '外部连接不能为空'
            },
            'content':{
                'required': '内容不能为空'
            }
        }