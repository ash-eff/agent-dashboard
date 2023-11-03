from django.db import models
from accounts.models import CustomUser


class Project(models.Model):
    project_name = models.CharField(max_length=255, unique=True)
    signature = models.TextField(max_length=400, default='Signature Goes Here', null=True)

    def __str__(self):
        return self.project_name


class UserProject(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'project']

    def __str__(self):
        return f'{self.user.username} - {self.project.project_name}'
