from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


class Enrollment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-enrolled_at']
        unique_together = ['owner', 'course']

    def __str__(self):
        return f'{self.owner} is enrolled in {self.course}'
