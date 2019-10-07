"""todo_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView, TaskView, TaskCreateView, UpdateView, DeleteView, TypeView, StatusView, \
    TypeCreateView, StatusCreateView, TypeUpdateView, StatusUpdateView, TypeDeleteView, StatusDeleteView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
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
    path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete')
]
