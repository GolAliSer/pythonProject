from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('task/', views.home, name='task'),
    path('category/<int:c_id>', views.tasks, name='tasks'),
    path('category/task/<int:task_id>/del', views.task_del, name='task_del'),
    path('add_category/', views.add_category, name='add_c'),
    path('category/<int:c_id>/del', views.category_del, name='c_del'),
    path('category/<str:category>/add_task', views.add_task, name='add_t'),

]