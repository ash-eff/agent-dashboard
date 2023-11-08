from rest_framework import serializers

from .models import EmailTemplate, OptionChoice, Placeholder


class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'body',
            'project',
        )
        model = EmailTemplate

    def create(self, validated_data):
        request = self.context.get('request')
        instance = EmailTemplate(**validated_data)
        instance.created_by = request.user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        request = self.context.get('request')
        instance.body = validated_data.get('body', instance.body)
        instance.project = validated_data.get('project', instance.project)
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

class PlaceholderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'placeholder_value',
            'type',
            'options',
            'email_template'
        )
        model = Placeholder

    def create(self, validated_data):
        request = self.context.get('request')
        instance = Placeholder(**validated_data)
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
