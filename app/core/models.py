from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email rather than username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Devicetype(models.Model):
    """Device type to be used for a device"""
    device_type = models.CharField(max_length=255)

    def __str__(self):
        return self.device_type


class Device(models.Model):
    """Device model to be used for each specific device"""
    device_id = models.IntegerField(primary_key=True)
    device_type = models.ForeignKey(
        'DeviceType',
        on_delete=models.SET_NULL,
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.device_id)


class Location(models.Model):
    """Location for a device"""
    loc_id = models.IntegerField(primary_key=True, editable=True)
    loc_name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.loc_id)


class Wxstatreading(models.Model):
    """Model fo weather station reading"""
    LocationID = models.ForeignKey(
        'location',
        on_delete=models.SET_NULL,
        null=True
    )
    LocationDescription = models.CharField(max_length=255, null=True)
    SystemType = models.CharField(max_length=255, null=True)
    deviceID = models.ForeignKey(
        'device',
        on_delete=models.SET_NULL,
        null=True
    )
    datetime = models.DateTimeField(null=True)
    air_temp = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    wind_avg_spd_kph = models.FloatField(null=True)
    wind_avg_direct = models.FloatField(null=True)
    wind_std_dev = models.IntegerField(null=True)
    rain_mm = models.FloatField(null=True)
    soil_temp = models.FloatField(null=True)
    solar_rad = models.FloatField(null=True)
    barometric = models.FloatField(null=True)
    evaporation = models.FloatField(null=True)
    air_temp_10_m = models.FloatField(null=True)
    air_temp_inversion = models.CharField(max_length=20, null=True)
    wind_direction_1 = models.CharField(max_length=20, null=True)
    wind_direction_2 = models.CharField(max_length=20, null=True)
    wind_dir_1_percent = models.IntegerField(null=True)
    wind_dir_2_percent = models.IntegerField(null=True)
    wind_speed_max = models.FloatField(null=True)
    wind_speed_min = models.FloatField(null=True)
    wind_speed_avg = models.FloatField(null=True)

    def __str__(self):
        return f"{self.device}__{self.datetime}"


class Soilprobereading(models.Model):
    """Model for soil probe reading"""
    LocationID = models.ForeignKey(
        'location',
        on_delete=models.SET_NULL,
        null=True
    )
    LocationDescription = models.CharField(max_length=255, null=True)
    SystemType = models.CharField(max_length=255, null=True)
    deviceID = models.ForeignKey(
        'device',
        on_delete=models.SET_NULL,
        null=True
    )
    datetime = models.DateTimeField(null=True)
    depth1 = models.FloatField(null=True)
    depth2 = models.FloatField(null=True)
    depth3 = models.FloatField(null=True)
    depth4 = models.FloatField(null=True)
    depth5 = models.FloatField(null=True)
    depth6 = models.FloatField(null=True)
    depth7 = models.FloatField(null=True)
    depth8 = models.FloatField(null=True)
    depth9 = models.FloatField(null=True)
    depth10 = models.FloatField(null=True)
    depth11 = models.FloatField(null=True)
    depth12 = models.FloatField(null=True)
    depth13 = models.FloatField(null=True)
    depth14 = models.FloatField(null=True)
    depth15 = models.FloatField(null=True)
    depth16 = models.FloatField(null=True)
    soiltotal = models.FloatField(null=True)
    rainfall = models.FloatField(null=True)
    irrigation_due_actual = models.FloatField(null=True)
    irrigation_due_default = models.FloatField(null=True)
    dailyuse = models.FloatField(null=True)
    temp = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    depth1temp = models.FloatField(null=True)
    depth2temp = models.FloatField(null=True)
    depth3temp = models.FloatField(null=True)
    depth4temp = models.FloatField(null=True)
    depth5temp = models.FloatField(null=True)
    depth6temp = models.FloatField(null=True)
    depth7temp = models.FloatField(null=True)
    depth8temp = models.FloatField(null=True)
    depth9temp = models.FloatField(null=True)
    depth10temp = models.FloatField(null=True)
    depth11temp = models.FloatField(null=True)
    depth12temp = models.FloatField(null=True)
    depth13temp = models.FloatField(null=True)
    depth14temp = models.FloatField(null=True)
    depth15temp = models.FloatField(null=True)
    depth16temp = models.FloatField(null=True)

    def __str__(self):
        return f"{self.deviceID}__{self.datetime}"


class Raingaugereading(models.Model):
    """Model for rain gauge reading"""
    LocationID = models.ForeignKey(
        'location',
        on_delete=models.SET_NULL,
        null=True
    )
    LocationDescription = models.CharField(max_length=255, null=True)
    SystemType = models.CharField(max_length=255, null=True)
    deviceID = models.ForeignKey(
        'device',
        on_delete=models.SET_NULL,
        null=True
    )
    rain = models.FloatField(null=True)
    datetime = models.DateTimeField(null=True)
    AccumulatedRain = models.FloatField(null=True)

    def __str__(self):
        return f"{self.deviceID}__{self.datetime}"


class Tankmonitorreading(models.Model):
    """Model for tank monitor reading"""
    LocationID = models.ForeignKey(
        'location',
        on_delete=models.SET_NULL,
        null=True
    )
    LocationDescription = models.CharField(max_length=255, null=True)
    SystemType = models.CharField(max_length=255, null=True)
    deviceID = models.ForeignKey(
        'device',
        on_delete=models.SET_NULL,
        null=True
    )
    datetime = models.DateTimeField(null=True)
    WaterHeightMillimeters = models.FloatField(null=True)
    RainFallMillimeters = models.FloatField(null=True)

    def __str__(self):
        return f"{self.deviceID}__{self.datetime}"
