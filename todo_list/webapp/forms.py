from django import forms
from django.forms import widgets
from webapp.models import Type, Status, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'full_description', 'status', 'type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['type']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
