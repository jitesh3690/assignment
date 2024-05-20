# task_manager/models.py
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('WIP', 'Work In Progress'),
        ('ONHOLD', 'On Hold'),
        ('DONE', 'Done'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='task')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.name