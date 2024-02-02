# Generated by Django 5.0.1 on 2024-01-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0031_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Languages', 'Languages'), ('Social Sciences', 'Social Sciences'), ('Art and Creativity', 'Art and Creativity'), ('Health and Fitness', 'Health and Fitness'), ('Design', 'Design'), ('Engineering', 'Engineering'), ('', 'Choose category'), ('Technology', 'Technology'), ('Business', 'Business'), ('Science', 'Science'), ('Marketing', 'Marketing'), ('Personal Development', 'Personal Development')], max_length=50),
        ),
    ]