# Generated by Django 5.0 on 2023-12-23 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_taskmodel_taskassigndate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='taskAssignDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]