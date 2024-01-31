# Generated by Django 5.0.1 on 2024-01-31 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_course_overall_rating_alter_course_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='overall_rating',
        ),
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Design', 'Design'), ('Art and Creativity', 'Art and Creativity'), ('Engineering', 'Engineering'), ('Social Sciences', 'Social Sciences'), ('Business', 'Business'), ('Marketing', 'Marketing'), ('Technology', 'Technology'), ('Science', 'Science'), ('Health and Fitness', 'Health and Fitness'), ('Languages', 'Languages'), ('Personal Development', 'Personal Development')], max_length=50),
        ),
    ]
