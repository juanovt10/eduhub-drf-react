from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rating


@receiver(post_save, sender=Rating)
def updated_course_overall_rating(sender, instance, **kwargs):
    course = instance.course
    ratings = Rating.objects.filter(course=course)
    rating_count = ratings.count()
    total_rating = sum([rating.rating for rating in ratings])
    if rating_count > 0:
        course.overall_rating = total_rating / rating_count
    else:
        course.overall_rating = None
    course.save()
