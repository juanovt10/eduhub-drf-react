# Generated by Django 5.0.1 on 2024-03-25 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0004_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-updated_at']},
        ),
        migrations.RemoveField(
            model_name='rating',
            name='title',
        ),
    ]
