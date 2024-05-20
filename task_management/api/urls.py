# urls.py
from django.urls import path, include
from .views import ProjectListAPIView, ProjectDetailAPIView, TaskListAPIView, TaskDetailAPIView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]
