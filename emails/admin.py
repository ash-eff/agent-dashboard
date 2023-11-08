from django.contrib import admin

from .models import EmailTemplate, Placeholder, OptionChoice

admin.site.register(EmailTemplate)
admin.site.register(Placeholder)
admin.site.register(OptionChoice)
