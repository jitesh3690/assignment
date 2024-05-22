from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.http import HttpResponseNotFound
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Project, Task, Client
from django.urls import reverse_lazy
from django.utils import timezone

def custom_404_view(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def homeView(request):
    return render(request, 'project_task/home.html')

class TaskListView(ListView):
    model = Task
    template_name = 'project_task/task_list.html'

class TaskCreateView(CreateView):
    model = Task
    fields = ['name', 'description', 'project', 'status']
    template_name = 'project_task/task_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['status']    #field to edit
    template_name = 'project_task/task_status.html'
    success_url = reverse_lazy('task_list')

def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse('No task with the given id', status=404)
    
    context = {'task': task}
    return render(request, 'project_task/task_detail.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'project_task/project_list.html'
    
    #modifying queryset to get project which are not ended (end date having future date)
    def get_queryset(self):
        return Project.objects.filter(end_date__gte=timezone.now())

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description', 'client', 'start_date', 'end_date']
    template_name = 'project_task/project_form.html'
    success_url = reverse_lazy('project_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.all()  # Add clients queryset to the context
        return context

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project_list')

def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse('No project with the given id', status=404)
    
    context = {'project': project}
    return render(request, 'project_task/project_detail.html', context)

def project_task_list(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse('No project with the given id', status=404)
    
    tasks = Task.objects.filter(project=project)
    if not tasks:
        tasks = None
    context = {
        'project': project,
        'tasks': tasks,
    }
    return render(request, 'project_task/project_task_list.html', context)

