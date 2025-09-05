from django.contrib import admin

from .models import Task, SubTask, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]

@admin.register(SubTask)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]

@admin.register(Category)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name"]