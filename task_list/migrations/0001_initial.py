# Generated by Django 4.2.1 on 2023-05-22 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateField()),
                ("is_completed", models.BooleanField()),
                (
                    "tag",
                    models.ManyToManyField(related_name="tasks", to="task_list.tag"),
                ),
            ],
        ),
    ]
