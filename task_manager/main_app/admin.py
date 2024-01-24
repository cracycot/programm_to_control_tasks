from django.contrib import admin

from .forms import TaskForm


# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    readonly_fields=('time_start', 'date_finish')
    form = TaskForm
