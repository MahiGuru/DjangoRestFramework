from django.db import models
from django.utils import timezone
from .user_model import User

# Create your models here.
class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    conf_code = models.CharField(max_length=50, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    meeting_date = models.DateField(default=timezone.now, null=True, blank=True)
    meeting_start_time = models.TextField(max_length=100, null=True, blank=True)
    meeting_end_time = models.TextField(max_length=100, null=True, blank=True)
    organizer_name = models.CharField(max_length=50, null=True, blank=True)
    organizer_email = models.EmailField(max_length=50, null=True, blank=True)
    invite_description = models.TextField(max_length=150, null=True, blank=True)
    meeting_title = models.CharField(max_length=50, null=True, blank=True)
    provider = models.CharField(max_length=50, blank=True, null=True)
    twilio_call_id = models.TextField(max_length=100)
    twilio_recording_id = models.TextField(max_length =60, null=True, blank=True)
    meeting_type = models.CharField(max_length=30, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    updated_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    subject = models.TextField(max_length=30, null=True, blank=True)
    lbc_order_id = models.TextField(max_length =60, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "meetings"