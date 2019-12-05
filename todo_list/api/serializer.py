from rest_framework import serializers


from webapp.models import Project, Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')