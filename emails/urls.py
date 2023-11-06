from django.urls import path

from .views import EmailTemplateList, EmailTemplateDetail

urlpatterns = [
    path('details/<int:pk>/', EmailTemplateDetail.as_view(), name='email_template_detail'),
    path('list/', EmailTemplateList.as_view(), name='email_template_list'),
]