from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Avg


COURSE_CATEGORIES=[
    ('', 'Choose category'),
    ('Technology', 'Technology'),
    ('Business', 'Business'),
    ('Design', 'Design'),
    ('Languages', 'Languages'),
    ('Personal Development', 'Personal Development'),
    ('Marketing', 'Marketing'),
    ('Science', 'Science'),
    ('Engineering', 'Engineering'),
    ('Social Sciences', 'Social Sciences'),
    ('Art and Creativity', 'Art and Creativity'),
    ('Health and Fitness', 'Health and Fitness'),
]


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to = 'images/', default='../course_default'
    )
    category = models.CharField(max_length=50, choices=COURSE_CATEGORIES, default='Technology')
    duration = models.DurationField()
    created_at = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    video_hours = models.DecimalField(max_digits=5, decimal_places=1)
    test_count = models.PositiveIntegerField(default=0)
    article_count = models.PositiveIntegerField(default=0)
    

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'


 