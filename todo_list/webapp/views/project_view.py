from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectIndexView(ListView):
    context_object_name = 'project'
    model = Project
    template_name = 'project/project_index.html'
    # paginate_by = 3
    # paginate_orphans = 1

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetailView(DetailView):
    template_name = 'project/project_view.html'
    context_object_name = 'project'
    model = Project


class ProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    context_object_name = 'project'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})
