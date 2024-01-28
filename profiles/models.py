from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    dob = models.DateField(
        verbose_name="Date of birth",
        null=True,
        blank=True,
        help_text="Please enter your date of birth in DD-MM-YYYY format.",
    )
    avatar = models.ImageField(
        upload_to = 'images/', default='../default_profile_m2rn8r'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile" 


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)