# Generated by Django 5.0.1 on 2024-01-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_instructor',
            field=models.BooleanField(default=False),
        ),
    ]
