from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'agent',
            'customer_name',
            'customer_email',
            'additional_customer_information',
            'case_number',
            'tid_number',
            'case_number_provided',
            'offered_additional_assistance',
            'case_notes',
        )
        model = Note
