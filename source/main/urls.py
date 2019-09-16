
from django.contrib import admin
from django.urls import path

from webapp.views import index_view, task_view, create_task_view, delete, update_task_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name = 'index'),
    path('task/<int:pk>/', task_view, name='task_view'),
    path('create/', create_task_view, name = 'create_view'),
    path('task/delete/<int:pk>/', delete, name='action_delete'),
    path('task/update/<int:pk>/', update_task_view, name='update_view')
]
