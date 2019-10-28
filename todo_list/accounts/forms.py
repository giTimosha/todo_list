from django.contrib.auth.models import User
from django import forms


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(label='логин')
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)
    first_name = forms.CharField(label='Имя', max_length=50, required=False)
    last_name = forms.CharField(label='Фамилия', max_length=50, required=False)
    email = forms.CharField(label='Email:', required=True)

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if not (first_name or last_name):
            raise forms.ValidationError('заполните имя или фамилия.')

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
