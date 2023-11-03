from rest_framework import generics

from .models import Note
from .permissions import IsOwnerOrReadOnly
from .serializers import NoteSerializer


class NoteList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = NoteSerializer

    # Custom method to get the queryset for listing notes
    def get_queryset(self):
        return Note.objects.filter(agent=self.request.user)

    # Custom method for creating a new note
    def create(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            request.data['agent'] = self.request.user.id
        return super().create(request, *args, **kwargs)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly, ]
    serializer_class = NoteSerializer

    # Custom method to get the queryset for retrieving a specific note
    def get_queryset(self):
        return Note.objects.filter(agent=self.request.user)
