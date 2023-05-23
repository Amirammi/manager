"""
URL configuration for manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import (
    index,
    TagListView,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    TagCreate,
    TagUpdate,
    TagDelete,
    TaskUpdateCompletionView
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreate.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdate.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDelete.as_view(), name="tag-delete"),
    path("tasks/create/", TaskCreate.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdate.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDelete.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/toggle/",
        TaskUpdateCompletionView.as_view(),
        name="task-toggle"
    )
]

app_name = "tasks"
