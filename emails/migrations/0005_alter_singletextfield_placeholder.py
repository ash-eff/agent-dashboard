# Generated by Django 4.2.6 on 2023-11-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0004_alter_singletextfield_placeholder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singletextfield',
            name='placeholder',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
