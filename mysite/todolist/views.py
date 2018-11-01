from django.shortcuts import render, redirect
from .models import TodoList


def index(request):
    todos = TodoList.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["title"]
            description = request.POST["description"]
            due_date = request.POST["due_date"]
            priority = request.POST["priority"]
            Todo = TodoList(title=title, description=description,
                            due_date=due_date, priority=priority)
            Todo.save()
            return redirect("/") #reloading the page

        if "taskDelete" in request.POST:
            checkedList = request.POST["deleteCheck"]
            for todo_id in checkedList:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, 'todolist/index.html')
