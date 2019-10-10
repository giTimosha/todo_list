from django.db import models
from django.shortcuts import render


class Project(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False, verbose_name='Name', default='')
    description = models.TextField(null=True, blank=True, verbose_name='description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='time of creation')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='change time')

    def __str__(self):
        return self.name


class Task(models.Model):
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name='Description')
    full_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Full description')
    status = models.ForeignKey('Status', related_name='task_status', verbose_name='Status', on_delete=models.PROTECT)
    type = models.ForeignKey('Type', related_name='task_type', verbose_name='type', on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True, null=False, blank=False, verbose_name='Date')
    project = models.ForeignKey(Project, null=True, blank=False, related_name='project', on_delete=models.PROTECT,
                                verbose_name='Project')

    def __str__(self):
        return self.description


class Status(models.Model):
    status = models.CharField(max_length=45, verbose_name='status')

    def __str__(self):
        return self.status


class Type(models.Model):
    type = models.CharField(max_length=45, verbose_name='type')

    def __str__(self):
        return self.type
