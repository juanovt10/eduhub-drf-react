from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to = 'images/', default='../default_profile_m2rn8r'
    )
    is_instructor = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)


class InstructorApplication(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    application_text = models.TextField()
    applied_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Application from {self.owner.username}'


@receiver(post_save, sender=InstructorApplication)
def approve_instructor_application(sender, instance, **kwargs):
    if instance.approved:
        profile, created = Profile.objects.get_or_create(owner=instance.owner)
        profile.is_instructor = True
        profile.save()
