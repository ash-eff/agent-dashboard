from django.db import models

from projects.models import Project


class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    singleTextFields = models.ManyToManyField('SingleTextField', blank=True)
    singleIntegerFields = models.ManyToManyField('SingleIntegerField', blank=True)
    multipleChoiceFields = models.ManyToManyField('MultipleChoiceField', blank=True)
    emailFields = models.ManyToManyField('EmailField', blank=True)
    textFields = models.ManyToManyField('TextField', blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)


class SingleTextField(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)


class SingleIntegerField(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()


class OptionChoice(models.Model):
    value = models.CharField(max_length=100)


class MultipleChoiceField(models.Model):
    name = models.CharField(max_length=50)
    options = models.ManyToManyField(OptionChoice)


class EmailField(models.Model):
    name = models.CharField(max_length=50)
    value = models.EmailField()


class TextField(models.Model):
    name = models.CharField(max_length=100)
    value = models.TextField()
