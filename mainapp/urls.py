#!/usr/bin/python3
# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('role/', views.role),
    path('', views.index)
]
