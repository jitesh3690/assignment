# Generated by Django 5.0.6 on 2024-05-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_task', '0003_alter_project_description_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='No Description Given'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, default='No Description Given'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'To Do'), ('WIP', 'Work In Progress'), ('ONHOLD', 'On Hold'), ('DONE', 'Done')], default='No Status Available', max_length=10),
        ),
    ]