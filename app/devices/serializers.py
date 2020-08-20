from rest_framework import serializers
from core.models import Device, Devicetype, Location, Wxstatreading


class DeviceSerializer(serializers.ModelSerializer):
    """Serializer for Device objects"""

    class Meta:
        model = Device
        fields = ('id', 'device_id')
        read_only_fields = ('id',)


class DevicetypeSerializer(serializers.ModelSerializer):
    """Serializer for Devicetype objects"""

    class Meta:
        model = Devicetype
        fields = ('id', 'device_type')
        read_only_fields = ('id',)


class LocationSerializer(serializers.ModelSerializer):
    """Serializer for Location objects"""

    class Meta:
        model = Location
        fields = ('id', 'loc_id', 'loc_name')
        read_only_fields = ('id',)


class WxstatreadingSerializer(serializers.ModelSerializer):
    """Serializer for weather station reading objects"""

    class Meta:
        model = Wxstatreading
        fields = (
            'id',
            'user',
            'loc',
            'device',
            'datetime',
            'air_temp',
            'humidity',
            'wind_avg_spd_kph',
            'wind_avg_direct',
            'wind_std_dev',
            'rain_mm',
            'soil_temp',
            'barometric',
            'air_temp_10_m',
            'air_temp_inversion',
            'wind_direction_1',
            'wind_direction_2',
            'wind_dir_1_percent',
            'wind_dir_2_percent',
            'wind_speed_max',
            'wind_speed_min',
            'wind_speed_avg',
        )
        read_only_fields = ('id', 'datetime')
