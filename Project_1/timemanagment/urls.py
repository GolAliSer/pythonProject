from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('task/', views.home, name='task'),
    path('category/<int:c_id>', views.tasks, name='tasks'),
    path('category/task/<int:task_id>/del', views.task_del, name='task_del'),
    path('dd_category/', views.add_category, name='add_c'),
]