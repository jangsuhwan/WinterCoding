from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse

def home(request):
    tasks = List.objects.all()
    now = datetime.datetime.now()
    nowDate = now.strftime("%Y-%m-%d")
    for task in tasks:
        if(task.due_date < nowDate):
            List.objects.filter(id=task.id).update(expired="expired")

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

def edit(request, task_id):
    task = List.objects.get(id = task_id)
    context = {'task' : task}
    return render (request, 'todolist/edit.html', context)

def update(request, task_id):
    List.objects.filter(id=task_id).update(**request.data)
    return home(request)