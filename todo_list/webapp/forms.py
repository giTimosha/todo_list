from django import forms
from django.forms import widgets
from webapp.models import Type, Status, Task


# class TaskForm(forms.Form):
#     description = forms.CharField(max_length=200, required=True, label='description')
#     full_description = forms.CharField(max_length=3000, required=False, label='Full description')
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), to_field_name='status', required=True, widget=forms.Select)
#     type = forms.ModelChoiceField(queryset=Type.objects.all(), to_field_name='type', required=True, widget=forms.Select)
#
#
# class StatusForm(forms.Form):
#     status = forms.CharField(max_length=45, label='status')
#
#
# class TypeForm(forms.Form):
#     type = forms.CharField(max_length=45, label='type')


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