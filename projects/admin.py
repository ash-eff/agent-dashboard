from django.contrib import admin

from .models import Project


class CustomProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'signature']
    fieldsets = [(None, {'fields': ['project_name', 'signature']})]


admin.site.register(Project, CustomProjectAdmin)

