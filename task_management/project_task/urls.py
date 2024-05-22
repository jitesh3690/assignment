from django.urls import path, include
from .views import (
    TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, task_detail, ProjectListView, ProjectCreateView, ProjectDeleteView,
    project_detail, project_task_list
)

urlpatterns = [
    # Task URLs
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/', task_detail, name='task_detail'),

    # Project URLs
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('projects/<int:pk>/tasks/', project_task_list, name='project_task_list'),

    #api
     path('', include('api.urls')),
]
