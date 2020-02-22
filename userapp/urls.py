#!/usr/bin/python3
# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('regist/', views.RegistView.as_view()),
    path('code/', views.send_code),
]
