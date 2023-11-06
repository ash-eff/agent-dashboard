from rest_framework import serializers

from .models import EmailTemplate, SingleTextField, SingleIntegerField, OptionChoice, MultipleChoiceField, EmailField, TextField


class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'body',
            'singleTextFields',
            'singleIntegerFields',
            'multipleChoiceFields',
            'emailFields',
            'textFields',
            'project',
        )
        model = EmailTemplate


class SingleTextFieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'value',
        )
        model = SingleTextField


class SingleIntegerFieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'value',
        )
        model = SingleIntegerField


class OptionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'value',
        )
        model = OptionChoice


class MultipleChoiceFieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'options',
        )
        model = MultipleChoiceField


class EmailFieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'value',
        )
        model = EmailField


class TextFieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'value',
        )
        model = TextField

