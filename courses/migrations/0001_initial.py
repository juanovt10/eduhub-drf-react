# Generated by Django 5.0.1 on 2024-03-29 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='../course_default', upload_to='images/')),
                ('category', models.CharField(choices=[('', 'Choose category'), ('Technology', 'Technology'), ('Business', 'Business'), ('Design', 'Design'), ('Languages', 'Languages'), ('Personal Development', 'Personal Development'), ('Marketing', 'Marketing'), ('Science', 'Science'), ('Engineering', 'Engineering'), ('Social Sciences', 'Social Sciences'), ('Art and Creativity', 'Art and Creativity'), ('Health and Fitness', 'Health and Fitness')], default='Technology', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('video_hours', models.DecimalField(decimal_places=1, max_digits=5)),
                ('test_count', models.PositiveIntegerField(default=0)),
                ('article_count', models.PositiveIntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
