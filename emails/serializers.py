from rest_framework import serializers

from .models import EmailTemplate, SimpleTextField, OptionChoice, MultipleChoiceField


class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'body',
            'simpleTextFields',
            'multipleChoiceFields',
            'project',
        )
        model = EmailTemplate

    def create(self, validated_data):
        request = self.context.get('request')
        simple_text_fields = validated_data.pop('simpleTextFields', None)
        multiple_choice_fields = validated_data.pop('multipleChoiceFields')
        instance = EmailTemplate(**validated_data)
        instance.created_by = request.user
        if simple_text_fields:
            instance.simpleTextFields.set(simple_text_fields)
        if multiple_choice_fields:
            instance.multipleChoiceFields.set(multiple_choice_fields)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.body = validated_data.get('body', instance.body)
        simple_text_fields = validated_data.get('simpleTextFields', instance.simpleTextFields.all())
        instance.simpleTextFields.set(simple_text_fields)
        multiple_choice_fields = validated_data.get('multipleChoiceFields', instance.multipleChoiceFields.all())
        instance.multipleChoiceFields.set(multiple_choice_fields)
        instance.project = validated_data.get('project', instance.project)
        instance.updated_by = request.user
        instance.save()
        return instance


class SimpleTextFieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'placeholder',
        )
        model = SimpleTextField

    def create(self, validated_data):
        request = self.context.get('request')
        instance = SimpleTextField(**validated_data)
        instance.created_by = request.user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.updated_by = request.user
        instance.save()
        return instance


class OptionChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'option',
        )
        model = OptionChoice

    def create(self, validated_data):
        request = self.context.get('request')
        instance = OptionChoice(**validated_data)
        instance.created_by = request.user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.updated_by = request.user
        instance.save()
        return instance

class MultipleChoiceFieldSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'options',
            'placeholder',
        )
        model = MultipleChoiceField

    def create(self, validated_data):
        request = self.context.get('request')
        instance = MultipleChoiceField(**validated_data)
        options = validated_data.pop('options', None)
        instance.created_by = request.user
        if options:
            instance.options.set(options)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get('request')
        options = validated_data.get('options', instance.options.all())
        instance.options.set(options)
        instance.updated_by = request.user
        instance.save()
        return instance
