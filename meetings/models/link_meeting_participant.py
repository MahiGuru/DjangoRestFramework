from django.db import models
from django.utils import timezone
from .meetings_model import Meeting
from .participant_model import Participant

# Create your models here.
class LinkMeetingParticipant(models.Model):
    id = models.AutoField(primary_key=True)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "link_meeting_participant"