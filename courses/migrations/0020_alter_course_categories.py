# Generated by Django 5.0.1 on 2024-01-31 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Design', 'Design'), ('Languages', 'Languages'), ('Personal Development', 'Personal Development'), ('Science', 'Science'), ('Engineering', 'Engineering'), ('Art and Creativity', 'Art and Creativity'), ('Business', 'Business'), ('Marketing', 'Marketing'), ('Social Sciences', 'Social Sciences'), ('Health and Fitness', 'Health and Fitness'), ('Technology', 'Technology')], max_length=50),
        ),
    ]
