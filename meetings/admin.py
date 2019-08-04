from django.contrib import admin
from .models import User
from .models import Meeting
from .models import MeetingItem
from .models import Participant
from .models import LinkMeetingParticipant


# Register your models here.
admin.site.register(User)
admin.site.register(Meeting)
admin.site.register(MeetingItem)
admin.site.register(Participant)
admin.site.register(LinkMeetingParticipant)