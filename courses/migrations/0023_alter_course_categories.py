# Generated by Django 5.0.1 on 2024-01-31 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Health and Fitness', 'Health and Fitness'), ('Languages', 'Languages'), ('Social Sciences', 'Social Sciences'), ('Marketing', 'Marketing'), ('Science', 'Science'), ('Engineering', 'Engineering'), ('Art and Creativity', 'Art and Creativity'), ('Design', 'Design'), ('Technology', 'Technology'), ('Personal Development', 'Personal Development'), ('Business', 'Business'), ('', 'Choose category')], max_length=50),
        ),
    ]
