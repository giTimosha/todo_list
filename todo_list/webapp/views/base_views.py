from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views.generic.base import View


class DetailView(TemplateView):
    context_key = 'object'
    model = None
    key_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_object()
        return context

    def get_object(self):
        pk = self.kwargs.get(self.key_kwarg)
        return get_object_or_404(self.model, pk=pk)


class UpdateView(View):
    form_class = None
    template_name = None
    redirect_url = ''
    model = None
    key_kwarg = 'pk'
    context_key = 'object'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(initial=self.get_form_initial())
        context = self.make_context(form)
        return render(request, self.template_name, context=context)

    def get_form_initial(self):
        model_fields = [field.name for field in self.model._meta.fields]
        initial = {}
        for field in model_fields:
            initial[field] = getattr(self.object, field)
        return initial

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = self.get_object()
        for field, value in form.cleaned_data.items():
            setattr(self.object, field, value)
        self.object.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        context = self.make_context(form)
        return render(self.request, self.template_name, context=context)

    def get_object(self):
        pk = self.kwargs.get(self.key_kwarg)
        return get_object_or_404(self.model, pk=pk)

    def make_context(self, form):
        return {
            'form': form,
            self.context_key: self.object
        }

    def get_redirect_url(self):
        return self.redirect_url


class DeleteView(View):
    model = None
    template_name = None
    redirect_url = ''
    context_object_name = None
    confirm_delete = True

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        return render(request, self.template_name, context={self.context_object_name: obj})

    def post(self, request, **kwargs):
        obj = self.get_object()
        obj.delete()
        return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return self.redirect_url

    def get_object(self):
        pk = self.kwargs.get('pk')
        print(self.model)
        obj = get_object_or_404(self.model, pk=pk)
        return obj
