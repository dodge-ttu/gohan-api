from rest_framework import serializers
from core.models import Device, Location


class DeviceSerializer(serializers.ModelSerializer):
    """Serializer for Device objects"""

    class Meta:
        model = Device
        fields = ('id', 'device_type')
        read_only_fields = ('id',)


class LocationSerializer(serializers.ModelSerializer):
    """Serializer for Location objects"""

    class Meta:
        model = Location
        fields = ('id', 'loc_id', 'loc_name')
        read_only_fields = ('id',)
