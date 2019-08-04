from rest_framework import serializers
from .models import User, Meeting


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 
        'remember_token', 'access_token', 'status', 'provider', 'provider_token', 'created_at', 'updated_at', 'image']


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Meeting
        fields = ('id', 'event_id', 'phone_number', 'conf_code', 'duration', 'meeting_date', 'meeting_start_time', 'meeting_end_time', 'organizer_name', 'organizer_email', 'invite_description', 'meeting_title', 'provider', 'twilio_call_id', 'twilio_recording_id', 'meeting_type', 'created_date', 'updated_date', 'subject', 'lbc_order_id', 'user')


