from django.db import models
from django.conf import settings


class Note(models.Model):
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    additional_customer_information = models.TextField(max_length=500, blank=True, null=True)
    case_number = models.IntegerField(blank=True, null=False)
    tid_number = models.IntegerField(blank=True, null=False)
    case_number_provided = models.BooleanField(default=False)
    offered_additional_assistance = models.BooleanField(default=False)
    case_notes = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f'{self.case_number} - {self.customer_name}'
