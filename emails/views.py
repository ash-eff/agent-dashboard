from rest_framework import generics

from .models import EmailTemplate
from .permissions import IsOwnerOrReadOnly
from .serializers import EmailTemplateSerializer


class EmailTemplateList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = EmailTemplateSerializer

    # Custom method to get the queryset for listing notes
    def get_queryset(self):
        return EmailTemplate.objects.all()

    # Custom method for creating a new note
    def create(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            request.data['agent'] = self.request.user.id
        return super().create(request, *args, **kwargs)


class EmailTemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = EmailTemplateSerializer

    # Custom method to get the queryset for retrieving a specific note
    def get_queryset(self):
        return EmailTemplate.objects.all()
