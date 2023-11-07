from django.contrib import admin

from .models import EmailTemplate, SimpleTextField, MultipleChoiceField, OptionChoice

admin.site.register(EmailTemplate)
admin.site.register(SimpleTextField)
admin.site.register(MultipleChoiceField)
admin.site.register(OptionChoice)
