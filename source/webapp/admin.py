from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'text', 'status']
    list_filter = ['status']
    search_fields = ['description', 'status','completed_at','text']
    fields = ['description', 'status', 'completed_at','text']


admin.site.register(Task, TaskAdmin)
