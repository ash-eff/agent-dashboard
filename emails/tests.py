from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import EmailTemplate, SimpleTextField, OptionChoice, MultipleChoiceField


class EmailTemplateTest(TestCase):
    @classmethod
    def SetUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='email@email.com',
            password='secret',
        )

        # cls.template = EmailTemplate.objects.create(
        #
        # )