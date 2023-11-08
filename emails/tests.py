from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import EmailTemplate, Placeholder, OptionChoice
from projects.models import Project


class EmailTemplateTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='Test User',
            email='email@email.com',
            password='secret',
        )

        cls.project = Project.objects.create(
            project_name='Test Project',
            signature='Test Signature',
        )

        cls.template = EmailTemplate.objects.create(
            name='Test Template',
            body='This is the test template body.',
            project=cls.project,
        )

        cls.option_one = OptionChoice.objects.create(
            option='Test Option One',
        )

        cls.option_two = OptionChoice.objects.create(
            option='Test Option Two',
        )

        cls.option_three = OptionChoice.objects.create(
            option='Test Option Three',
        )

        cls.placeholder_simple = Placeholder.objects.create(
            name='Placeholder Simple',
            type='Simple Text Field',
            email_template=cls.template,
        )

        cls.placeholder_multiple_one = Placeholder.objects.create(
            name='Placeholder Multiple',
            type='Multiple Choice Field One',
            email_template=cls.template,
        )

        cls.placeholder_multiple_one.options.add(cls.option_one, cls.option_two)

        cls.placeholder_multiple_two = Placeholder.objects.create(
            name='Placeholder Multiple',
            type='Multiple Choice Field One',
            email_template=cls.template,
        )

        cls.placeholder_multiple_two.options.add(cls.option_one, cls.option_two, cls.option_three)

    def test_email_template(self):
        self.assertEqual(self.template.name, 'Test Template')
        self.assertEqual(self.template.body, 'This is the test template body.')
        self.assertEqual(self.template.project.project_name, 'Test Project')

    def test_placeholder_options(self):
        self.assertEqual(self.placeholder_simple.options.count(), 0)
        self.assertEqual(self.placeholder_multiple_one.options.count(), 2)
        self.assertEqual(self.placeholder_multiple_two.options.count(), 3)

    def test_template_list_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse('email_template_list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_template_details_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        template_pk = 1
        url = reverse('email_template_detail', kwargs={'pk': template_pk})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_placeholder_list_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse('placeholder_list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_placeholder_details_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        template_pk = 1
        url = reverse('placeholder_detail', kwargs={'pk': template_pk})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_options_list_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse('option_choice_list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_options_details_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        template_pk = 1
        url = reverse('option_choice_detail', kwargs={'pk': template_pk})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
