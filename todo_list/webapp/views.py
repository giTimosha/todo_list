from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView

from webapp.forms import TaskForm, StatusForm, TypeForm
from webapp.models import Task, Type, Status

class Indexview(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context



class CreateView(TemplateView):

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



class UpdateView(TemplateView):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data={'description': task.description, 'full_description': task.full_description, 'status': task.status, 'type': task.type})
        return render(request, 'update.html', context={'form': form, 'task': task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task.description = data['description']
            task.full_description = data['full_description']
            task.status = data['status']
            task.type = data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update.html', context={'form': form})


class DeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'delete.html', context={'task': task})

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])

        task.delete()
        return redirect('index')

class TypeView(TemplateView):

    template_name = 'types.html'

    def get_context_data(self, **kwargs):
        type = super().get_context_data(**kwargs)
        type['types'] = Type.objects.all()
        return type



class StatusView(TemplateView):

    template_name = 'status_view.html'

    def get_context_data(self, **kwargs):
        task = super().get_context_data(**kwargs)
        task['statuses'] = Status.objects.all()
        return task



class TypeCreateView(TemplateView):

    def get(self, request, **kwargs):
        type = TypeForm()
        return render(request, 'type_create.html', context={'task': type})

    def post(self, request, *args, **kwargs):
        type = TypeForm(data=request.POST)
        if type.is_valid():
            data = type.cleaned_data
            Type.objects.create(type=data['type'])
            return redirect('types_view')
        else:
            return render(request, 'type_create.html', context={'task': type})



class StatusCreateView(TemplateView):

    def get(self, request, **kwargs):
        status = StatusForm()
        return render(request, 'status_create.html', context={'form': status})

    def post(self, request, *args, **kwargs):
        status = StatusForm(data=request.POST)
        if status.is_valid():
            data = status.cleaned_data
            Status.objects.create(status=data['status'])
            return redirect('status_view')
        else:
            return render(request, 'status_create.html', context={'form': status})


class TypeUpdateView(TemplateView):

    def get(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data={'type': type})
        return render(request, 'type_update.html', context={'form': form, 'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        task = TypeForm(data=request.POST)
        if task.is_valid():
            data = task.cleaned_data
            type.type = data['type']
            type.save()
            return redirect('types_view')
        else:
            return render(request, 'type_update.html', context={'task': task})


class StatusUpdateView(TemplateView):

    def get(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data={'status': status})
        return render(request, 'status_update.html', context={'form': form, 'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        task = StatusForm(data=request.POST)
        if task.is_valid():
            data = task.cleaned_data
            status.status = data['status']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'status_update.html', context={'task': task})



class TypeDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        return render(request, 'type_delete.html', context={'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])

        type.delete()
        return redirect('types_view')



class StatusDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status_delete.html', context={'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])

        status.delete()
        return redirect('status_view')