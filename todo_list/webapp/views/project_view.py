from django.views.generic import ListView, DetailView

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
