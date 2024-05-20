from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from .models import Project, Task, Client
from django.urls import reverse_lazy
from django.utils import timezone

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
    fields = ['status']
    template_name = 'project_task/task_status.html'
    success_url = reverse_lazy('task_list')
    

class ProjectListView(ListView):
    model = Project
    template_name = 'project_task/project_list.html'
    
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

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_task/project_detail.html'

class ProjectTaskListView(ListView):
    model = Task
    template_name = 'project_task/project_task_list.html'

    def get_queryset(self):
        self.project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return Task.objects.filter(project=self.project)

