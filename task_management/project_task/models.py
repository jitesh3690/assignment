# task_manager/models.py
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Client(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='No Description Given')
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def clean(self):
        super().clean()
        if self.start_date and self.start_date > timezone.now().date():
            raise ValidationError("Start date cannot be in the future.")
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("End date cannot be before start date.")
        
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
    description = models.TextField(blank=True, default='No Description Given')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='task')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='No Status Available')
    
    def __str__(self):
        return self.name