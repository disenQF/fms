#!/usr/bin/python3
# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('role/', views.role),
    path('', views.index)
]
