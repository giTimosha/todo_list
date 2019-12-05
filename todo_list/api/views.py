from rest_framework import viewsets

from api.serializer import ProjectSerializer, TaskSerializer
from webapp.models import Project, Task


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer