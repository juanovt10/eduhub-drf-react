from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from django.core.validators import MinValueValidator, MaxValueValidator


class Rating(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        ordering = ['created_at']
        unique_together = ['owner', 'course']

    def __str__(self):
        return f'{self.owner} {self.course}'

