from django.contrib import admin
from django.urls import path, include, re_path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('create/', views.create, name="create"),
    #path('update/(<int:task_id>)/', views.update, name="update"),
    path('delete/<int:task_id>/', views.delete,
        name="delete-task")
]
