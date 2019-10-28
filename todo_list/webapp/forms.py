from django import forms
from django.forms import widgets
from webapp.models import Type, Status, Task, Project
from django.contrib.auth.models import User



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


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")
