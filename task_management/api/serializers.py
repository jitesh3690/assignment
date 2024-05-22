# serializers.py
from rest_framework import serializers
from project_task.models import Project, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProjectListSerializer(serializers.ModelSerializer):
    task = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
        
class ProjectDetailSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
