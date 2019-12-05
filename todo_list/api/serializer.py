from rest_framework import serializers

from webapp.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 'description', 'full_description', 'status',
            'type', 'date', 'project')

class ProjectSerializer(serializers.ModelSerializer):
    task_project = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at', 'task_project')