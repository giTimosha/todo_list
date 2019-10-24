from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from webapp.forms import StatusForm
from webapp.models import Status
from webapp.views.base_views import DeleteView


class StatusView(ListView):
    template_name = 'status/status_view.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return Status.objects.all()


class StatusCreateView(LoginRequiredMixin, CreateView):
    template_name = 'status/status_create.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_view')


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'status/status_update.html'
    context_object_name = 'status'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_view')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    template_name = 'status/status_delete.html'

    def get_redirect_url(self):
        return reverse('status_view')
