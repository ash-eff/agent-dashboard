from django.contrib import admin

from .models import Project, UserProject


class CustomProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'signature']
    fieldsets = [(None, {'fields': ['project_name', 'signature']})]


class CustomUserProjectAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'is_admin']
    fieldsets = [(None, {'fields': ['user', 'project', 'is_admin']})]


admin.site.register(Project, CustomProjectAdmin)
admin.site.register(UserProject, CustomUserProjectAdmin)
