# Generated by Django 5.0.6 on 2024-05-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(),
        ),
    ]
