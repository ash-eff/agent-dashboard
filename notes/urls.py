from django.urls import path

from .views import NoteList, NoteDetail

urlpatterns = [
    path('details/<int:pk>/', NoteDetail.as_view(), name='note_detail'),
    path('list/', NoteList.as_view(), name='note_list'),
]
