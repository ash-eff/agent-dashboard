from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=255, unique=True)
    signature = models.TextField(max_length=400, default='Signature Goes Here', null=True)

    def __str__(self):
        return self.project_name
