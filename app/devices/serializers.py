from rest_framework import serializers
from core.models import Device, Devicetype, Location, Wxstatreading, \
    Soilprobereading, Raingaugereading, Tankmonitorreading


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
        read_only_fields = ('id', 'datetime',)


class SoilprobereadingSerializers(serializers.ModelSerializer):
    """Serializer for soil probe reading objects"""

    class Meta:
        model = Soilprobereading
        fields = (
            'user',
            'loc',
            'device',
            'datetime',
            'depth1',
            'depth2',
            'depth3',
            'depth4',
            'depth5',
            'depth6',
            'depth7',
            'depth8',
            'depth9',
            'depth10',
            'depth11',
            'depth12',
            'depth13',
            'depth14',
            'depth15',
            'depth16',
            'soiltotal',
            'rainfall',
            'irrigation_due_actual',
            'irrigation_due_default',
            'dailyuse',
            'temp',
            'humidity',
            'depth1temp',
            'depth2temp',
            'depth3temp',
            'depth4temp',
            'depth5temp',
            'depth6temp',
            'depth7temp',
            'depth8temp',
            'depth9temp',
            'depth10temp',
            'depth11temp',
            'depth12temp',
            'depth13temp',
            'depth14temp',
            'depth15temp',
            'depth16temp',
        )
        read_only_fields = ('id', 'datetime',)


class RaingaugereadingSerializer(serializers.ModelSerializer):
    """Serializer for rain gauge objects"""

    class Meta:
        model = Raingaugereading
        fields = (
            'user',
            'loc',
            'device',
            'datetime',
            'rain',
            'accum_rain',
        )
        read_only_fields = ('id', 'datetime')


class TankmonitorreadingSerializer(serializers.ModelSerializer):
    """Serializer for tank monitor objects"""

    class Meta:
        model = Tankmonitorreading
        fields = (
            'user',
            'loc',
            'device',
            'datetime',
            'water_height_mm',
            'rainfall_mm',
        )
        read_only_fields = ('id', 'datetime')
