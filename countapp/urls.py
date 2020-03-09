
from django.urls import path, include
from . import views

urlpatterns = [
    path('block/', views.block_cnt),
    path('user/', views.user_cnt),

]
