from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/notes/', include('notes.urls')),
    path('api/v1/templates/', include('emails.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
