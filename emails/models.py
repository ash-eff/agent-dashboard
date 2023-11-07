from django.db import models

from projects.models import Project
from accounts.models import CustomUser


class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    simpleTextFields = models.ManyToManyField('SimpleTextField', blank=True)
    multipleChoiceFields = models.ManyToManyField('MultipleChoiceField', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_template')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='updated_template')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def replace_placeholders(self, data):
        for placeholder, value in data.items():
            self.body = self.body.replace(f'{{{placeholder}}}', value)
        return self.body


class SimpleTextField(models.Model):
    name = models.CharField(max_length=50)
    placeholder = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_text_field')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='updated_text_field')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholder_name = self.name.casefold().replace(' ', '-')
        self.placeholder = f'{{{placeholder_name}}}'


class OptionChoice(models.Model):
    option = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_option')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='updated_option')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MultipleChoiceField(models.Model):
    name = models.CharField(max_length=50)
    options = models.ManyToManyField(OptionChoice)
    placeholder = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_multiple')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='updated_multiple')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholder_name = self.name.casefold().replace(' ', '-')
        self.placeholder = f'{{{placeholder_name}}}'
