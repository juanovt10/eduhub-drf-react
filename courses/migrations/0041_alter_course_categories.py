# Generated by Django 5.0.1 on 2024-01-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0040_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('', 'Choose category'), ('Technology', 'Technology'), ('Business', 'Business'), ('Design', 'Design'), ('Languages', 'Languages'), ('Personal Development', 'Personal Development'), ('Marketing', 'Marketing'), ('Science', 'Science'), ('Engineering', 'Engineering'), ('Social Sciences', 'Social Sciences'), ('Art and Creativity', 'Art and Creativity'), ('Health and Fitness', 'Health and Fitness')], default='Technology', max_length=50),
        ),
    ]