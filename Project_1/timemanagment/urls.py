from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', views.index, name='home'),
    path('task/', views.home, name='tasks')
]