# Generated by Django 5.0.1 on 2024-01-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_remove_course_overall_rating_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Marketing', 'Marketing'), ('Technology', 'Technology'), ('Social Sciences', 'Social Sciences'), ('Languages', 'Languages'), ('Science', 'Science'), ('Health and Fitness', 'Health and Fitness'), ('Personal Development', 'Personal Development'), ('Engineering', 'Engineering'), ('Art and Creativity', 'Art and Creativity'), ('Business', 'Business'), ('Design', 'Design')], max_length=50),
        ),
    ]
