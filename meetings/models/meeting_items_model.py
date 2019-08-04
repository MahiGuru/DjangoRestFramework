from django.db import models
from django.utils import timezone
from .meetings_model import Meeting

# Create your models here.
class MeetingItem(models.Model):
    id = models.AutoField(primary_key=True)
    item_text = models.TextField(max_length=30, blank=True, null=True)
    item_type = models.CharField(max_length=80, blank=True, null=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    updated_item_type = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_date = models.DateTimeField(default=timezone.now, blank=True, null=True)    
    updated_item_text = models.CharField(max_length=100, blank=True, null=True)
    item_task = models.CharField(max_length=80, blank=True, null=True)
    speaker = models.EmailField(max_length=50, blank=True, null=True) 

    class Meta:
        db_table = "meeting_items"