from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView

from webapp.forms import TypeForm
from webapp.models import Type
from webapp.views import UpdateView
from webapp.views.base_views import DeleteView


class TypeView(ListView):
    template_name = 'type/types.html'
    context_object_name = 'types'

    def get_queryset(self):
        return Type.objects.all()


class TypeCreateView(CreateView):
    template_name = 'task/create.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class TypeUpdateView(UpdateView):
    form_class = TypeForm
    template_name = 'type/type_update.html'
    model = Type
    context_object_name = 'type'

    def get_redirect_url(self):
        return reverse('types_view')


class TypeDeleteView(DeleteView):
    model = Type
    context_object_name = 'type'
    template_name = 'type/type_delete.html'

    def get_redirect_url(self):
        return reverse('types_view')
