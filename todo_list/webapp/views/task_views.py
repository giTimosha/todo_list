from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from webapp.forms import TaskForm, SimpleSearchForm
from webapp.models import Task


class IndexView(ListView):
    context_object_name = 'tasks'
    model = Task
    template_name = 'task/index.html'
    # ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(description__icontains=self.search_value) | Q(full_description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class TaskView(DetailView):
    template_name = 'task/view.html'
    context_key = 'task'
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task/create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/update.html'
    context_object_name = 'task'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'task/delete.html'

    def get_success_url(self):
        return reverse('webapp:index')
