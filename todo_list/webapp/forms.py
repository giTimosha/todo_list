from django import forms
from django.forms import widgets
from webapp.models import Type, Status


class TaskForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='description')
    full_description = forms.CharField(max_length=3000, required=False, label='Full description')
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, widget=forms.Select)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True, widget=forms.Select)