# Generated by Django 5.0.1 on 2024-01-31 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Health and Fitness', 'Health and Fitness'), ('Science', 'Science'), ('Languages', 'Languages'), ('Art and Creativity', 'Art and Creativity'), ('Marketing', 'Marketing'), ('', 'Choose category'), ('Business', 'Business'), ('Technology', 'Technology'), ('Social Sciences', 'Social Sciences'), ('Engineering', 'Engineering'), ('Personal Development', 'Personal Development'), ('Design', 'Design')], max_length=50),
        ),
    ]
