# Generated by Django 4.0.4 on 2022-05-23 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]