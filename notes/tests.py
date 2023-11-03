from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Note


class NoteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='email@email.com',
            password='secret',
        )

        cls.otherUser = get_user_model().objects.create_user(
            username='testuser2',
            email='email2@email.com',
            password='secret2',
        )

        cls.note = Note.objects.create(
            agent=cls.user,
            customer_name='Demo Customer',
            customer_email='email@email.com',
            additional_customer_information='additional information.',
            case_number='123456',
            tid_number='7890',
            case_number_provided=True,
            offered_additional_assistance=True,
            case_notes='These are case notes.'
        )

    # Test note creation for user
    def test_note_model(self):
        self.assertEqual(self.note.agent.username, 'testuser')
        self.assertEqual(self.note.customer_name, 'Demo Customer')
        self.assertEqual(self.note.customer_email, 'email@email.com')
        self.assertEqual(self.note.additional_customer_information, 'additional information.')
        self.assertEqual(self.note.case_number, '123456')
        self.assertEqual(self.note.case_number_provided, True)
        self.assertEqual(self.note.offered_additional_assistance, True)
        self.assertEqual(self.note.case_notes, 'These are case notes.')

    # Test that the user can access the note list of notes they created
    def test_note_list_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse('note_list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test that an unauthorized user cannot access the note list
    def test_note_list_access_denied(self):
        client = APIClient()
        url = reverse('note_list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test that the user can access the note details for notes they have created
    def test_note_detail_access(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        note_pk = 1
        url = reverse('note_detail', kwargs={'pk': note_pk})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test that an unauthorized user cannot access the note details
    def test_note_detail_access_denied(self):
        client = APIClient()
        note_pk = 1
        url = reverse('note_detail', kwargs={'pk': note_pk})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test that another authorized user cannot access the notes created by other users
    def test_note_list_access_denied_two(self):
        client = APIClient()
        client.force_authenticate(user=self.otherUser)
        note_pk = 1
        url = reverse('note_detail', kwargs={'pk': note_pk})
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
