
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.getLogin, name='login'),
    path('logout/', views.getLogout, name='logout'),
    path('create/', views.getcreate, name='create'),
    path('profile/', views.getProfile, name='profile'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('complete/<list_id>', views.complete, name='complete'),
    path('register/', views.getRegister, name='register'),
]
