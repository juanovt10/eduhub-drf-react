# Generated by Django 5.0.1 on 2024-01-31 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Personal Development', 'Personal Development'), ('Art and Creativity', 'Art and Creativity'), ('Languages', 'Languages'), ('Social Sciences', 'Social Sciences'), ('Technology', 'Technology'), ('Marketing', 'Marketing'), ('Science', 'Science'), ('Design', 'Design'), ('Health and Fitness', 'Health and Fitness'), ('Business', 'Business'), ('', 'Choose category'), ('Engineering', 'Engineering')], max_length=50),
        ),
    ]
