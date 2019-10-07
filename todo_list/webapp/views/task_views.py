from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from webapp.forms import TaskForm
from webapp.models import Task
from webapp.views.base_views import DetailView, UpdateView, DeleteView


class IndexView(ListView):
    context_object_name = 'tasks'
    model = Task
    template_name = 'task/index.html'
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get_queryset(self):
        return Task.objects.all()


class TaskView(DetailView):
    template_name = 'task/view.html'
    context_key = 'task'
    model = Task


class TaskCreateView(CreateView):
    template_name = 'task/create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(UpdateView):
    form_class = TaskForm
    template_name = 'task/update.html'
    model = Task
    context_object_name = 'task'

    def get_redirect_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/delete.html'

    def get_redirect_url(self):
        return reverse('index')

