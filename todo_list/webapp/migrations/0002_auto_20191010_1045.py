# Generated by Django 2.2.5 on 2019-10-10 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='time of creation')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='change time')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project', to='webapp.Project', verbose_name='heading'),
        ),
    ]
