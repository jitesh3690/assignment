
from django.urls import path, include
from .views import ProjectListAPIView, ProjectDetailAPIView, TaskListAPIView, TaskDetailAPIView, api_home

urlpatterns = [
    path('', api_home, name='api_home'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]
