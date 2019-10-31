from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from accounts.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


def login_view(request):
    context = {}
    error = request.GET.get('next')
    test = request.session.setdefault('test', error)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if error == None:
                return redirect('webapp:index')
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):

    logout(request)

    return redirect('webapp:index')


def register_view(request, *args, **kwargs):

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:index')
    else:
        form = UserCreationForm()

    return render(request, 'create.html', context={'form': form})


class UserListView(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'


class UserDetailView(DetailView):

    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserPersonalInfoChangeView(UpdateView):
    model = User

    template_name = 'user_info_change.html'

    form_class = UserChangeForm

    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.object.pk})


class UserPasswordChangeView(UpdateView):
    model = User

    template_name = 'user_password_change.html'

    form_class = PasswordChangeForm

    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('accounts:login')
