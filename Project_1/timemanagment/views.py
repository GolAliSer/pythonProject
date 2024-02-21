from django.shortcuts import render

def index(request):
    return render(request, 'timemanagment/main.html')
def task(request):
    return render(request, 'timemanagment/task.html')

