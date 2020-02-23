#!/usr/bin/python3
# coding: utf-8
from django.urls import path
from . import views


urlpatterns = [
    path('code/', views.send_code),
    path('regist/', views.RegistView.as_view()),
    path('files/', views.FileView.as_view()),
    path('download/', views.download),
    path('create_img_link/', views.create_image_link),
    path('show_img/', views.show_img),

]
