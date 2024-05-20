from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, ProjectListView, ProjectCreateView, ProjectDeleteView,
    ProjectDetailView, ProjectTaskListView
)

urlpatterns = [
    # Task URLs
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),

    # Project URLs
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/create/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/tasks/', ProjectTaskListView.as_view(), name='project_task_list'),
]
