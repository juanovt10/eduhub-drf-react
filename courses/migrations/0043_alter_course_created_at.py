# Generated by Django 5.0.1 on 2024-03-01 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0042_rename_categories_course_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
