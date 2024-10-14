from django.shortcuts import render
from .models import Task

def index(request):
    return render(request,"index.html")


def add_todo_view(request):
    if request.method == 'POST':
        todo = request.POST.get("todo")
        
        todo_data = Task(title=todo, user=request.user)
        todo_data.save()
        return render("Home")

    return render(request,"index.html")