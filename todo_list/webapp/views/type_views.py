from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

from webapp.forms import TypeForm
from webapp.models import Type


class TypeView(ListView):
    template_name = 'type/types.html'
    context_object_name = 'types'

    def get_queryset(self):
        return Type.objects.all()


class TypeCreateView(TemplateView):

    def get(self, request, **kwargs):
        form = TypeForm()
        return render(request, 'type/type_create.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(
                type=form.cleaned_data['type']
            )
            return redirect('types_view')
        else:
            return render(request, 'type/type_create.html', context={'type': type})


class TypeUpdateView(TemplateView):

    def get(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data={'type': type})
        return render(request, 'type/type_update.html', context={'form': form, 'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        task = TypeForm(data=request.POST)
        if task.is_valid():
            data = task.cleaned_data
            type.type = data['type']
            type.save()
            return redirect('types_view')
        else:
            return render(request, 'type/type_update.html', context={'task': task})


class TypeDeleteView(TemplateView):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        return render(request, 'type/type_delete.html', context={'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])

        type.delete()
        return redirect('types_view')