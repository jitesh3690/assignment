from django.shortcuts import render
from rest_framework import generics
from project_task.models import Project, Task
from .serializers import ProjectListSerializer, ProjectDetailSerializer, TaskSerializer
from rest_framework.pagination import PageNumberPagination

def api_home(request):
    return render(request, 'project_task/api_home.html')

class FiveItemsPerPagePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class ProjectListAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    pagination_class = FiveItemsPerPagePagination

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer

class TaskListAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = FiveItemsPerPagePagination

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
