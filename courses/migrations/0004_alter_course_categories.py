# Generated by Django 5.0.1 on 2024-01-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_rename_descirption_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Art and Creativity', 'Art and Creativity'), ('Design', 'Design'), ('Health and Fitness', 'Health and Fitness'), ('Technology', 'Technology'), ('Business', 'Business'), ('Languages', 'Languages'), ('Social Sciences', 'Social Sciences'), ('Personal Development', 'Personal Development'), ('Engineering', 'Engineering'), ('', 'Course category'), ('Marketing', 'Marketing'), ('Science', 'Science')], max_length=50),
        ),
    ]
