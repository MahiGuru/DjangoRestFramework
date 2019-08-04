from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.SlugField(max_length=30)
    last_name = models.SlugField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    activation_key = models.SlugField(blank=True, null=True)
    remember_token = models.SlugField(blank=True, null=True)
    access_token = models.SlugField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    provider = models.CharField(max_length=30)
    provider_token = models.SlugField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    image = models.SlugField(max_length=30);