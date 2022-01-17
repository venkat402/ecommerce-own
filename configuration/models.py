from django.db import models


# Create your models here.


class Configuration(models.Model):
    site_name = models.CharField(max_length=255, default='')
    site_url = models.CharField(max_length=255, default='')
    contact_details = models.CharField(max_length=255, default='')
    email = models.EmailField(default='')
    mobile = models.CharField(max_length=20, default='')
    logo = models.ImageField(upload_to='site_logo', default='')
    favicon = models.ImageField(upload_to='site_favicon', default='')
    banner = models.ImageField(upload_to='site_banner', default='')
    address = models.TextField(default='')
    payments = models.TextField(default='')
    languages = models.JSONField(default=dict())
    currencies = models.JSONField(default=dict())
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
