# Generated by Django 4.2.7 on 2023-11-03 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255, unique=True)),
                ('signature', models.TextField(default='Signature Goes Here', max_length=400, null=True)),
            ],
        ),
    ]
