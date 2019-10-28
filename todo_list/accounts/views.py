from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from webapp.forms import UserCreationForm


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