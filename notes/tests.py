from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Note


class NoteTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='email@email.com',
            password='secret',
        )

        cls.note = Note.objects.create(
            agent_id=cls.user,
            customer_name='Demo User',
            case_number='123456',
            tid_number='7890',
            case_number_provided=True,
            offered_additional_assistance=True,
            case_notes='These are case notes.'
        )

    def test_note_model(self):
        self.assertEqual(self.note.agent_id.username, 'testuser')
        self.assertEqual(self.note.customer_name, 'Demo User')
        self.assertEqual(self.note.case_number, '123456')
        self.assertEqual(self.note.case_number_provided, True)
        self.assertEqual(self.note.offered_additional_assistance, True)
        self.assertEqual(self.note.case_notes, 'These are case notes.')
