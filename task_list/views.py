from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag
from .forms import TaskForm, TagForm


def index(request):
    context = {
        "tasks": Task.objects.prefetch_related("tags"),
    }
    return render(request, "tasks/index.html", context=context)


def toggle_complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True
    task.save()
    return HttpResponseRedirect(reverse_lazy(
        "tasks:index"
    ))


class TagListView(generic.ListView):
    model = Tag


class TagCreate(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdate(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class TagDelete(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


class TaskCreate(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskUpdate(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskDelete(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")
