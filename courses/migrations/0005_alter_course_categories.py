# Generated by Django 5.0.1 on 2024-01-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Social Sciences', 'Social Sciences'), ('Business', 'Business'), ('Technology', 'Technology'), ('Engineering', 'Engineering'), ('Art and Creativity', 'Art and Creativity'), ('Marketing', 'Marketing'), ('Science', 'Science'), ('Health and Fitness', 'Health and Fitness'), ('Personal Development', 'Personal Development'), ('', 'Course category'), ('Languages', 'Languages'), ('Design', 'Design')], max_length=50),
        ),
    ]