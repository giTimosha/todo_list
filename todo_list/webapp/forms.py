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


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']
