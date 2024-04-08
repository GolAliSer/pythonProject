from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'timemanagment/main.html')

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'timemanagment/task.html', context)

def tasks (request, c_id):
    category = Category.objects.get(pk=c_id)
    tasks = Tasks.objects.filter(category=category).filter(is_done=False)
    category = category.title
    context = {
        'tasks': tasks,
        'category': category
    }
    return render(request, 'timemanagment/tasks.html', context)

def description(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    context = {
        'task': task,
    }
    return render(request, 'timemanagment/description.html', context)