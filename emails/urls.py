from django.urls import path

from .views import EmailTemplateList, EmailTemplateDetail, PlaceholderList, PlaceholderDetail, OptionChoiceList, OptionChoiceDetail

urlpatterns = [
    path('email/details/<int:pk>/', EmailTemplateDetail.as_view(), name='email_template_detail'),
    path('email/list/', EmailTemplateList.as_view(), name='email_template_list'),
    path('placeholder/details/<int:pk>/', PlaceholderDetail.as_view(), name='placeholder_detail'),
    path('placeholder/list/', PlaceholderList.as_view(), name='placeholder_list'),
    path('option-choice/details/<int:pk>/', OptionChoiceDetail.as_view(), name='option_choice_detail'),
    path('option-choice/list/', OptionChoiceList.as_view(), name='option_choice_list'),
]
