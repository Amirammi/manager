from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag
from .forms import TaskForm


def index(request):
    context = {
        "tasks": Task.objects.prefetch_related("tags"),
    }
    return render(request, "task_list/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag


class TaskCreate(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list:index")


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_list:index")


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_list:index")
