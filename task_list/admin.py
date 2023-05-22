from django.contrib import admin
from django.contrib.auth.models import Group

from models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "datetime",
        "is_completed",
        "deadline",
    )
    list_filter = ("is_completed",)
    search_fields = ("name",)


admin.site.register(Tag)
admin.site.unregister(Group)
