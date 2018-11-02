from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    tasks = List.objects.all
    return render (request, 'todolist/list.html', {'tasks' : tasks})

def add(request):
    return render (request, 'todolist/add.html',)
