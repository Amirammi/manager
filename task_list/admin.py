from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "datetime",
        "is_completed",
        "deadline",
    )
    list_filter = ("is_completed",)
    search_fields = ("content",)


admin.site.register(Tag)
admin.site.unregister(Group)
