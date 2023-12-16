from rest_framework import serializers
from .models import Events

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ('__all__')