# Generated by Django 4.2.1 on 2023-05-22 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_list", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline",
            field=models.DateField(blank=True, null=True),
        ),
    ]
