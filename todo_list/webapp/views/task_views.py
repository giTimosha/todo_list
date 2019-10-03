from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

from webapp.forms import TaskForm
from webapp.models import Task


class Indexview(ListView):
    template_name = 'task/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()


class TaskView(TemplateView):
    template_name = 'task/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class CreateView(TemplateView):

    def get(self, request, **kwargs):
        form = TaskForm()
        return render(request, 'task/create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task.objects.create(description=data['description'], full_description=data['full_description'], status=data['status'], type=data['type'])
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task/create.html', context={'form': form})


class UpdateView(TemplateView):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data={'description': task.description, 'full_description': task.full_description, 'status': task.status, 'type': task.type})
        return render(request, 'task/update.html', context={'form': form, 'task': task})

    def post(self, request, **kwargs):
        form = TaskForm(data=request.POST)
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.full_description = form.cleaned_data['full_description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task/update.html', context={'form': form})


class DeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'task/delete.html', context={'task': task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])

        task.delete()
        return redirect('index')
