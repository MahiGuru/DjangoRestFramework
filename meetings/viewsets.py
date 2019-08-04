from django.shortcuts import render
from .models import User, Meeting
from rest_framework import viewsets
from .serializers import UserSerializer, MeetingSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created_at').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class MeetingViewSet(viewsets.ModelViewSet): 
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer