# Generated by Django 4.2.6 on 2023-11-07 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_remove_emailfield_template_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionchoice',
            name='value',
        ),
        migrations.AddField(
            model_name='emailfield',
            name='placeholder',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='multiplechoicefield',
            name='placeholder',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='optionchoice',
            name='placeholder',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='singleintegerfield',
            name='placeholder',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='singletextfield',
            name='placeholder',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='textfield',
            name='placeholder',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]