#!/usr/bin/python3
# coding: utf-8

from django import forms
from .models import TSysRole


class RoleForm(forms.ModelForm):
    class Meta:
        model = TSysRole
        fields = ['name', 'code']
        error_messages = {
            'name': {
                'required': '角色名不能为空'
            },
            'code': {
                'required': '角色代码不能为空'
            }
        }