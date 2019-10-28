from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from webapp.forms import TypeForm
from webapp.models import Type


class TypeView(ListView):
    template_name = 'type/types.html'
    context_object_name = 'types'

    def get_queryset(self):
        return Type.objects.all()


class TypeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'task/create.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('webapp:types_view')


class TypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Type
    template_name = 'type/type_update.html'
    context_object_name = 'type'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('webapp:types_view')


class TypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Type
    context_object_name = 'type'
    template_name = 'type/type_delete.html'

    def get_success_url(self):
        return reverse_lazy('webapp:types_view')
