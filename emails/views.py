from rest_framework import generics

from .models import EmailTemplate, SimpleTextField, MultipleChoiceField, OptionChoice
from .permissions import IsOwnerOrReadOnly
from .serializers import EmailTemplateSerializer, SimpleTextFieldSerializer, MultipleChoiceFieldSerializer, OptionChoiceSerializer


class EmailTemplateList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = EmailTemplateSerializer

    # Custom method to get the queryset for listing notes
    def get_queryset(self):
        return EmailTemplate.objects.all()


class EmailTemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = EmailTemplateSerializer

    # Custom method to get the queryset for retrieving a specific note
    def get_queryset(self):
        return EmailTemplate.objects.all()


class SimpleTextFieldList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = SimpleTextFieldSerializer

    def get_queryset(self):
        return SimpleTextField.objects.all()


class SimpleTextFieldDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = SimpleTextFieldSerializer

    # Custom method to get the queryset for retrieving a specific note
    def get_queryset(self):
        return SimpleTextField.objects.all()


class MultipleChoiceFieldList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = MultipleChoiceFieldSerializer

    def get_queryset(self):
        return MultipleChoiceField.objects.all()


class MultipleChoiceFieldDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = MultipleChoiceFieldSerializer

    # Custom method to get the queryset for retrieving a specific note
    def get_queryset(self):
        return MultipleChoiceField.objects.all()


class OptionChoiceList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = OptionChoiceSerializer

    def get_queryset(self):
        return OptionChoice.objects.all()



class OptionChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = OptionChoiceSerializer

    def get_queryset(self):
        return OptionChoice.objects.all()
