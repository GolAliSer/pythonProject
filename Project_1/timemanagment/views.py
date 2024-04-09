from django.shortcuts import render, redirect
from .models import *
from forms import *

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

def task_del(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    task.is_done = True
    task.save()
    category = task.category.id
    return redirect(tasks, c_id=category)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    else:
        form = CategoryForm
        context = {
            'form': form
        }
        return render(request, 'timemanagment/add_category.html', context)