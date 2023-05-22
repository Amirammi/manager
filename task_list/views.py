from django.shortcuts import render
from django.views import generic

from .models import Task, Tag


def index(request):
    context = {
        "tasks": Task.objects.prefetch_related("tags"),
    }
    return render(request, "task_list/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
