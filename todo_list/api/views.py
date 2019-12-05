from rest_framework import viewsets

from api.serializer import ProjectSerializer
from webapp.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer