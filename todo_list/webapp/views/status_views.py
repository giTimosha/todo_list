from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView

from webapp.forms import StatusForm
from webapp.models import Status
from webapp.views.base_views import UpdateView


class StatusView(ListView):
    template_name = 'status/status_view.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return Status.objects.all()


class StatusCreateView(CreateView):
    template_name = 'status/status_create.html'
    model = Status
    form_class = StatusForm

    def get_success_url(self):
        return reverse('status_index')


class StatusUpdateView(UpdateView):
    form_class = StatusForm
    template_name = 'status/status_update.html'
    model = Status
    context_object_name = 'status'

    def get_redirect_url(self):
        return reverse('status_view')


class StatusDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status/status_delete.html', context={'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])

        status.delete()
        return redirect('status_view')
