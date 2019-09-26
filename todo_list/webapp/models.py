from django.db import models
from django.shortcuts import render


class Task(models.Model):
    description = models.TextField(max_length=200, null=False, blank=False, verbose_name='Description')
    full_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Full description')
    status = models.ForeignKey('Status', related_name='task_status', verbose_name='Status', on_delete=models.PROTECT)
    type = models.ForeignKey('Type', related_name='task_type', verbose_name='type', on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True, null=False, blank=False, verbose_name='Date')

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