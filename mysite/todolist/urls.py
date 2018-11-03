from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('create/', views.create, name="create"),
    path('edit/<int:task_id>/', views.edit, name="update"),
    path('delete/<int:task_id>/', views.delete, name="delete")
]
