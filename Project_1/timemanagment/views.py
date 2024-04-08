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

def tasks (request, category):
    tasks = Tasks.objects.filter(category=category).filter(is_done=False)
    context = {
        'tasks': tasks
    }
    return render(request, 'timemanagment/task.html', context)