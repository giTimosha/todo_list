from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

from webapp.forms import StatusForm
from webapp.models import Status


class StatusView(ListView):
    template_name = 'status/status_view.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return Status.objects.all()


class StatusCreateView(TemplateView):

    def get(self, request, **kwargs):
        status = StatusForm()
        return render(request, 'status/status_create.html', context={'form': status})

    def post(self, request, *args, **kwargs):
        status = StatusForm(data=request.POST)
        if status.is_valid():
            data = status.cleaned_data
            Status.objects.create(status=data['status'])
            return redirect('status_view')
        else:
            return render(request, 'status/status_create.html', context={'form': status})


class StatusUpdateView(TemplateView):

    def get(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data={'status': status})
        return render(request, 'status/status_update.html', context={'form': form, 'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        task = StatusForm(data=request.POST)
        if task.is_valid():
            data = task.cleaned_data
            status.status = data['status']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'status/status_update.html', context={'task': task})


class StatusDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status/status_delete.html', context={'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])

        status.delete()
        return redirect('status_view')