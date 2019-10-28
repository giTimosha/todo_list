from django.urls import path
from .views import IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView, \
    TypeView, TypeCreateView, TypeUpdateView, TypeDeleteView, StatusView, StatusCreateView, StatusUpdateView, StatusDeleteView,\
    ProjectIndexView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/add', TaskCreateView.as_view(), name='create_view'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='update_view'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='delete_view'),
    path('types/', TypeView.as_view(), name='types_view'),
    path('statuses/', StatusView.as_view(), name='status_view'),
    path('types/add/', TypeCreateView.as_view(), name='type_create'),
    path('status/add/', StatusCreateView.as_view(), name='status_create'),
    path('types/<int:pk>/edit/', TypeUpdateView.as_view(), name='type_update'),
    path('status/<int:pk>/edit/', StatusUpdateView.as_view(), name='status_update'),
    path('types/<int:pk>/delete/', TypeDeleteView.as_view(), name='type_delete'),
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('projects/', ProjectIndexView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_view'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
]

app_name = 'webapp'
