from django.db import models

from projects.models import Project
from accounts.models import CustomUser


class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_template')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='updated_template')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.project.project_name}'


class OptionChoice(models.Model):
    option = models.CharField(max_length=50, blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_option')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='updated_option')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.option}'


class Placeholder(models.Model):
    name = models.CharField(max_length=50)
    placeholder_value = models.CharField(max_length=75)
    TYPE_CHOICES = (
        ('simple', 'Simple Text Field'),
        ('multiple_choice', 'Multiple Choice Field'),
        ('text', 'Full Text Field'),
    )

    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    options = models.ManyToManyField(OptionChoice, blank=True)
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE, related_name='placeholders')
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_placeholder')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='updated_placeholder')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholder_name = self.name.casefold().replace(' ', '-')
        self.placeholder_value = f'{{{placeholder_name}}}'

    def __str__(self):
        return f'Placeholder in Email Template: {self.email_template.name}'
