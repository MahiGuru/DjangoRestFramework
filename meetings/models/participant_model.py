from django.db import models
from django.utils import timezone
from .meetings_model import Meeting

# Create your models here.
class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    participant_name = models.TextField(max_length=30, blank=True, null=True)
    participant_email = models.EmailField(max_length=80, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    class Meta:
        db_table = "participant"