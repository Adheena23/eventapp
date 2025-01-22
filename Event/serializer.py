from rest_framework import serializers
from .models import Event, Attendee

class EventSerializer(serializers.ModelSerializer):
    attendees_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'date', 'time', 'location', 'attendees_count']

    def get_attendees_count(self, obj):
        return obj.attendees.count()

class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['id', 'user', 'event']


