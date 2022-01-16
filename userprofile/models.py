from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default=None, upload_to='profile_images')
    mobile = models.CharField(max_length=20, default=None, blank=True, null=True)
    address1 = models.CharField(max_length=255, default=None, blank=True, null=True)
    address2 = models.CharField(max_length=255, default=None, blank=True, null=True)
    city = models.CharField(max_length=100, default=None, blank=True, null=True)
    state = models.CharField(max_length=100, default=None, blank=True, null=True)
    country = models.CharField(max_length=100, default=None, blank=True, null=True)
    zip = models.CharField(max_length=10, default=None, blank=True, null=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
