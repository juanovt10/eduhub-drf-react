# Generated by Django 5.0.1 on 2024-01-31 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_alter_course_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.CharField(choices=[('Social Sciences', 'Social Sciences'), ('Health and Fitness', 'Health and Fitness'), ('Art and Creativity', 'Art and Creativity'), ('Personal Development', 'Personal Development'), ('Technology', 'Technology'), ('Engineering', 'Engineering'), ('Marketing', 'Marketing'), ('Design', 'Design'), ('Science', 'Science'), ('Languages', 'Languages'), ('Business', 'Business')], max_length=50),
        ),
    ]
