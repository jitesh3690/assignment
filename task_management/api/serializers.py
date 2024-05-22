# serializers.py
from rest_framework import serializers
from project_task.models import Project, Task
from django.utils import timezone
from datetime import datetime

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

def validate_start_date(value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Start date wont be future date")
        return value

def validate_end_date(value):
    if value < timezone.now().date():
        raise serializers.ValidationError("End date can't be in the past")
    return value

class ProjectListSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField(many=True, read_only=True)
    start_date = serializers.DateField(validators=[validate_start_date])
    end_date = serializers.DateField(validators=[validate_end_date])

    class Meta:
        model = Project
        fields = '__all__'

    
class ProjectDetailSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True, read_only=True)
    start_date = serializers.DateField(validators=[validate_start_date])
    end_date = serializers.DateField(validators=[validate_end_date])

    class Meta:
        model = Project
        fields = '__all__'
