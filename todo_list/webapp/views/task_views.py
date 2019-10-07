from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView
from webapp.forms import TaskForm
from webapp.models import Task
from webapp.views.base_views import DetailView


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
