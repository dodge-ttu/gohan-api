from rest_framework import serializers
from core.models import Device, Devicetype, Location, Wxstatreading, \
    Soilprobereading, Raingaugereading, Tankmonitorreading


def create_weather_stat_reading(r, loc_obj, sys_type, dev_obj):
    """Create weather station object in database from array"""
    wx_obj = Wxstatreading.objects.create(
        LocationID=loc_obj,
        LocationDescription=loc_obj.loc_name,
        SystemType=sys_type,
        deviceID=dev_obj,
        air_temp=r.get('AirTemp', None),
        humidity=r.get('Humidity', None),
        wind_avg_spd_kph=r.get('WindAvgSpdKph', None),
        wind_avg_direct=r.get('WindAvgDirect', None),
        wind_std_dev=r.get('WindStdDev', None),
        rain_mm=r.get('Rainmm', None),
        soil_temp=r.get('SoilTemp', None),
        solar_rad=r.get('SolarRad', None),
        barometric=r.get('Barometric', None),
        evaporation=r.get('Evaporation', None),
        air_temp_10_m=r.get('AirTemp10M', None),
        air_temp_inversion=r.get('AirTempInversion', None),
        wind_direction_1=r.get('WindDirection1', None),
        wind_direction_2=r.get('WindDirection2', None),
        wind_dir_1_percent=r.get('WindDirection1Percent', None),
        wind_dir_2_percent=r.get('WindDirection2Percent', None),
        wind_speed_max=r.get('WindSpeedMax', None),
        wind_speed_min=r.get('WindSPeedMin', None),
        wind_speed_avg=r.get('WindSPeedAvg', None)
    )
    return wx_obj


def create_soil_probe_reading(r, loc_obj, sys_type, dev_obj):
    """Create a soil probe object in database from array row"""
    sp_obj = Soilprobereading.objects.create(
        LocationID=loc_obj,
        LocationDescription=loc_obj.loc_name,
        SystemType=sys_type,
        deviceID=dev_obj,
        datetime=r.get('datetime', None),
        depth1=r.get('depth1', None),
        depth2=r.get('depth2', None),
        depth3=r.get('depth3', None),
        depth4=r.get('depth4', None),
        depth5=r.get('depth5', None),
        depth6=r.get('depth6', None),
        depth7=r.get('depth7', None),
        depth8=r.get('depth8', None),
        depth9=r.get('depth9', None),
        depth10=r.get('depth10', None),
        depth11=r.get('depth11', None),
        depth12=r.get('depth12', None),
        depth13=r.get('depth13', None),
        depth14=r.get('depth14', None),
        depth15=r.get('depth15', None),
        depth16=r.get('depth16', None),
        soiltotal=r.get('soiltotal', None),
        rainfall=r.get('rainfall', None),
        irrigation_due_actual=r.get('IrrigationDueActual', None),
        irrigation_due_default=r.get('IrrigationDueDefault', None),
        dailyuse=r.get('DailyUse', None),
        temp=r.get('temp', None),
        humidity=r.get('Humidity', None),
        depth1temp=r.get('depth1Temp', None),
        depth2temp=r.get('depth2Temp', None),
        depth3temp=r.get('depth3Temp', None),
        depth4temp=r.get('depth4Temp', None),
        depth5temp=r.get('depth5Temp', None),
        depth6temp=r.get('depth6Temp', None),
        depth7temp=r.get('depth7Temp', None),
        depth8temp=r.get('depth8Temp', None),
        depth9temp=r.get('depth9Temp', None),
        depth10temp=r.get('depth10Temp', None),
        depth11temp=r.get('depth11Temp', None),
        depth12temp=r.get('depth12Temp', None),
        depth13temp=r.get('depth13Temp', None),
        depth14temp=r.get('depth14Temp', None),
        depth15temp=r.get('depth15Temp', None),
        depth16temp=r.get('depth16Temp', None)
    )
    return sp_obj


def create_rain_gauge_reading(r, loc_obj, sys_type, dev_obj):
    """Creat rain gauge object in database from array row"""
    datetime = r.get('datetime', None)
    rain = r.get('rain', None)
    accum_rain = r.get('AccumulatedRain', None)
    rgr = Raingaugereading.objects.create(
        LocationID=loc_obj,
        LocationDescription=loc_obj.loc_name,
        SystemType=sys_type,
        deviceID=dev_obj,
        rain=rain,
        datetime=datetime,
        AccumulatedRain=accum_rain
    )
    return rgr


def create_tank_monitor_reading(r, loc_obj, sys_type, dev_obj):
    """Create tank monitor object in database from array row"""
    datetime = r.get('DateTime', None)
    water_height_mm = r.get('WaterHeightMillimetres', None)
    rainfall_mm = r.get('RainFallMillimeters', None)
    tmr = Tankmonitorreading.objects.create(
        LocationID=loc_obj,
        LocationDescription=loc_obj.loc_name,
        SystemType=sys_type,
        deviceID=dev_obj,
        datetime=datetime,
        WaterHeightMillimeters=water_height_mm,
        RainFallMillimeters=rainfall_mm
    )
    return tmr


class DeviceSerializer(serializers.ModelSerializer):
    """Serializer for Device objects"""

    class Meta:
        model = Device
        fields = ('device_id',)


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
        fields = ('loc_id', 'loc_name')


class WxstatreadingSerializer(serializers.ModelSerializer):
    """Serializer for weather station reading objects"""

    class Meta:
        model = Wxstatreading
        fields = (
            'LocationID',
            'LocationDescription',
            'SystemType',
            'deviceID',
            'datetime',
            'air_temp',
            'humidity',
            'wind_avg_spd_kph',
            'wind_avg_direct',
            'wind_std_dev',
            'rain_mm',
            'soil_temp',
            'solar_rad',
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

        def create(self, validated_data):
            """Custom create method for the Goanna Ag data structure"""
            loc_obj = validated_data.get('LocationID', None)
            system_type = validated_data.get('SystemType', None)
            devices = validated_data.get('Devices', None)
            if devices is not None:
                sensor_data = devices.get('WeatherStations', None)
                device_obj = sensor_data.get('deviceID', None)
                device_obj = Device.objects.get(pk=device_obj)
                data_array = sensor_data.get('deviceDataArray', None)

                if data_array is not None:
                    wxrs = []
                    for row in data_array:
                        wxr = create_weather_stat_reading(
                            r=row,
                            loc_obj=loc_obj,
                            sys_type=system_type,
                            dev_obj=device_obj
                        )
                        wxrs.append(wxr)
                    return wxrs
            else:
                device = validated_data.get('deviceID', None)
                device_obj = Device.objects.get(pk=device)
                row = validated_data
                wxr = create_weather_stat_reading(
                    r=row,
                    loc_obj=loc_obj,
                    sys_type=system_type,
                    dev_obj=device_obj
                )
                return wxr


class SoilprobereadingSerializers(serializers.ModelSerializer):
    """Serializer for soil probe reading objects"""
    Devices = serializers.JSONField(allow_null=True)

    class Meta:
        model = Soilprobereading
        fields = (
            'LocationID',
            'LocationDescription',
            'SystemType',
            'deviceID',
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
            'Devices',
        )

    def create(self, validated_data):
        """Custom create method for the Goanna Ag data structure"""
        loc_obj = validated_data.get('LocationID', None)
        system_type = validated_data.get('SystemType', None)
        devices = validated_data.get('Devices', None)
        if devices is not None:
            sensor_data = devices.get('Probes', None)
            device_obj = sensor_data.get('deviceID', None)
            device_obj = Device.objects.get(pk=device_obj)
            data_array = sensor_data.get('deviceDataArray', None)

            if data_array is not None:
                sprs = []
                for row in data_array:
                    spr = create_soil_probe_reading(
                            r=row,
                            loc_obj=loc_obj,
                            sys_type=system_type,
                            dev_obj=device_obj
                        )
                    sprs.append(spr)
                return sprs
        else:
            device = validated_data.get('deviceID', None)
            device_obj = Device.objects.get(pk=device)
            row = validated_data
            spr = create_soil_probe_reading(
                        r=row,
                        loc_obj=loc_obj,
                        sys_type=system_type,
                        dev_obj=device_obj
                    )
            return spr


class RaingaugereadingSerializer(serializers.ModelSerializer):
    """Serializer for rain gauge objects"""
    Devices = serializers.JSONField(allow_null=True)

    class Meta:
        model = Raingaugereading
        fields = (
            'LocationID',
            'LocationDescription',
            'SystemType',
            'deviceID',
            'rain',
            'datetime',
            'AccumulatedRain',
            'Devices',
        )

    def create(self, validated_data):
        """Custom create method for the Goanna Ag data structure"""
        loc_obj = validated_data.get('LocationID', None)
        system_type = validated_data.get('SystemType', None)
        devices = validated_data.get('Devices', None)
        if devices is not None:
            sensor_data = devices.get('RainGauges', None)
            device_obj = sensor_data.get('deviceID', None)
            device_obj = Device.objects.get(pk=device_obj)
            data_array = sensor_data.get('deviceDataArray', None)

            if data_array is not None:
                rgrs = []
                for row in data_array:
                    rgr = create_rain_gauge_reading(
                           r=row,
                           loc_obj=loc_obj,
                           sys_type=system_type,
                           dev_obj=device_obj
                    )
                    rgrs.append(rgr)

                return rgrs
        else:
            device = validated_data.get('deviceID', None)
            device_obj = Device.objects.get(pk=device)
            row = validated_data
            rgr = create_rain_gauge_reading(
                r=row,
                loc_obj=loc_obj,
                sys_type=system_type,
                dev_obj=device_obj,
            )
            return rgr


class TankmonitorreadingSerializer(serializers.ModelSerializer):
    """Serializer for tank monitor objects"""
    Devices = serializers.JSONField(allow_null=True)

    class Meta:
        model = Tankmonitorreading
        fields = (
            'LocationID',
            'LocationDescription',
            'SystemType',
            'deviceID',
            'datetime',
            'WaterHeightMillimeters',
            'RainFallMillimeters',
            'Devices'
        )

    def create(self, validated_data):
        """Custom create method for the Goanna Ag data structure"""
        loc_obj = validated_data.get('LocationID', None)
        system_type = validated_data.get('SystemType', None)
        devices = validated_data.get('Devices', None)
        if devices is not None:
            sensor_data = devices.get('TankMonitors', None)
            device_obj = sensor_data.get('deviceID', None)
            device_obj = Device.objects.get(pk=device_obj)
            data_array = sensor_data.get('deviceDataArray', None)

            print(validated_data)

            if data_array is not None:
                tmrs = []
                for row in data_array:
                    tmr = create_tank_monitor_reading(
                        r=row,
                        loc_obj=loc_obj,
                        sys_type=system_type,
                        dev_obj=device_obj
                    )
                    tmrs.append(tmr)
                return tmrs
        else:
            device = validated_data.get('deviceID', None)
            device_obj = Device.objects.get(pk=device)
            row = validated_data
            tmr = create_tank_monitor_reading(
                r=row,
                loc_obj=loc_obj,
                sys_type=system_type,
                dev_obj=device_obj
            )
            return tmr
