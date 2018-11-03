from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    tasks = List.objects.all
    return render (request, 'todolist/list.html', {'tasks' : tasks})

def add(request):
    return render (request, 'todolist/add.html',)

def create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
        return home(request)
    else:
        form = ListForm()

    return home(request)

def delete(request, task_id):
    task = List.objects.get(id=task_id)
    task.delete()
    return home(request)
