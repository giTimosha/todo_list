from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task, Type, Status

class Indexview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class Task_view(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context



class Create_View(TemplateView):

    def get(self, request, **kwargs):
        form = TaskForm()
        return render(request, 'create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task.objects.create(description=data['description'], full_description=data['full_description'], status=data['status'], type=data['type'])
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'create.html', context={'form': form})



class Update_View(TemplateView):

    def get(self, request, *args, **kwargs):
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        form = TaskForm(data={
            'description': task.description,
            'status': task.status,
            'type': task.type
        })
        return render(request, 'update.html', context={
            'form': form,
            'task': task
        })

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        task_pk = kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_pk)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()

            return redirect('task_detail', pk=task_pk)
        else:
            return render(request, 'update.html', context={
                'form': form,
                'task': task,
            })