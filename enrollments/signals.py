from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enrollment

@receiver(post_save, sender=Enrollment)
def remove_course_from_wishlist(sender, instance, created, **kwargs):
    if created:
        from wish_lists.models import WishList
        WishList.objects.filter(owner=instance.owner, course=instance.course).delete()