from django.db import models
from django.conf import settings


class Note(models.Model):
    agent_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    case_number = models.IntegerField()
    tid_number = models.IntegerField()
    case_number_provided = models.BooleanField(default=False)
    offered_additional_assistance = models.BooleanField(default=False)
    case_notes = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.case_number} - {self.agent_id.name}'
