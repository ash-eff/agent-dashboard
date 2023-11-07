from django.urls import path

from .views import EmailTemplateList, EmailTemplateDetail, SimpleTextFieldList, SimpleTextFieldDetail, MultipleChoiceFieldList, MultipleChoiceFieldDetail, OptionChoiceList, OptionChoiceDetail

urlpatterns = [
    path('email/details/<int:pk>/', EmailTemplateDetail.as_view(), name='email_template_detail'),
    path('email/list/', EmailTemplateList.as_view(), name='email_template_list'),
    path('simple-field/details/<int:pk>/', SimpleTextFieldDetail.as_view(), name='simple_text_detail'),
    path('simple-field/list/', SimpleTextFieldList.as_view(), name='simple_text_list'),
    path('multiple-choice/details/<int:pk>/', MultipleChoiceFieldDetail.as_view(), name='multiple_choice_detail'),
    path('multiple-choice/list/', MultipleChoiceFieldList.as_view(), name='multiple_choice_list'),
    path('option-choice/details/<int:pk>/', OptionChoiceDetail.as_view(), name='option_choice_detail'),
    path('option-choice/list/', OptionChoiceList.as_view(), name='option_choice_list'),
]
