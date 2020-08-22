from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@iamdodge.us', password='TestPass123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@iamdodge.us'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@iaMdoDGe.us'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        email = None
        password = 'TestPass123'
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=email,
                password=password,
            )

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@iamdodge.us',
            password='TestPass123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_devicetype_string(self):
        """Test the device type string representation"""
        devicetype = models.Devicetype.objects.create(
            device_type='Soil Moisture Probe'
        )

        self.assertEqual(str(devicetype), devicetype.device_type)

    def test_location_string(self):
        """Test the location string representation"""
        location = models.Location.objects.create(
            user=sample_user(),
            loc_id='23111',
            loc_name='Dodge low water',
        )
        self.assertEqual(str(location), location.loc_name)

    def test_wxstatreading_string(self):
        """Test creation of weather station reading"""
        user = sample_user()
        aloc = models.Location.objects.create(
            loc_id=12345,
            loc_name='Johnson Farm',
            user=user
        )
        adevicetype = models.Devicetype.objects.create(
            device_type='Soil Moisture Probe'
        )
        adevice = models.Device.objects.create(
            device_id=12455,
            device_type=adevicetype,
            user=user
        )
        wxstatreading = models.Wxstatreading.objects.create(
            user=user,
            loc=aloc,
            device=adevice,
            datetime="2020-06-01T21:10:24.000Z",
            air_temp=13.75,
            humidity=44.2,
            wind_avg_spd_kph=9.81,
            wind_avg_direct=250.38,
            wind_std_dev=-1,
            rain_mm=0,
            soil_temp=40.2,
            barometric=1015.4,
            evaporation=6.34,
            air_temp_10_m=23.74,
            air_temp_inversion=1,
            wind_direction_1='WSW',
            wind_direction_2='N',
            wind_dir_1_percent=100,
            wind_dir_2_percent=0,
            wind_speed_max=12.86,
            wind_speed_min=8.10,
            wind_speed_avg=9.61,
        )
        string_match = f"{wxstatreading.device}__{wxstatreading.datetime}"
        self.assertEqual(str(wxstatreading), string_match)

    def test_soilprobereading_string(self):
        """Test soil probe reading model returns string"""
        user = sample_user()
        aloc = models.Location.objects.create(
            loc_id=12345,
            loc_name='Johnson Farm',
            user=user
        )
        adevicetype = models.Devicetype.objects.create(
            device_type='Soil Moisture Probe'
        )
        adevice = models.Device.objects.create(
            device_id=11123,
            device_type=adevicetype,
            user=user
        )
        soilprobereading = models.Soilprobereading.objects.create(
            user=user,
            loc=aloc,
            device=adevice,
            datetime="2020-06-01T21:10:24.000Z",
            depth1=32.4,
            depth2=32.4,
            depth3=32.4,
            depth4=39.4,
            depth5=32.4,
            depth6=37.4,
            depth7=32.4,
            depth8=52.4,
            depth9=32.4,
            depth10=42.4,
            depth11=32.4,
            depth12=32.4,
            depth13=22.4,
            depth14=32.4,
            depth15=12.4,
            depth16=32.4,
            soiltotal=232.4,
            rainfall=52.4,
            irrigation_due_actual=200.43,
            irrigation_due_default=100.32,
            dailyuse=1.8,
            temp=34,
            humidity=65,
            depth1temp=18,
            depth2temp=17,
            depth3temp=18,
            depth4temp=18,
            depth5temp=28,
            depth6temp=18,
            depth7temp=17,
            depth8temp=18,
            depth9temp=38,
            depth10temp=18,
            depth11temp=78,
            depth12temp=18,
            depth13temp=18,
            depth14temp=28,
            depth15temp=18,
            depth16temp=68
        )
        string_match = f"{soilprobereading.device}__{soilprobereading.datetime}"
        self.assertEqual(str(soilprobereading), string_match)

    def test_raingaugereading_string(self):
        """Test rain guage model returns string"""
        user = sample_user()
        aloc = models.Location.objects.create(
            loc_id=12345,
            loc_name='Johnson Farm',
            user=user
        )
        adevicetype = models.Devicetype.objects.create(
            device_type='Soil Moisture Probe'
        )
        adevice = models.Device.objects.create(
            device_id=11123,
            device_type=adevicetype,
            user=user
        )
        raingaugereading = models.Raingaugereading.objects.create(
            loc_id=aloc,
            loc_name=aloc.loc_name,
            device_id=adevice,
            system_type='Metric',
            datetime="2020-06-01T21:10:24.000Z",
            rain=0.2,
            accum_rain=45.6,
        )
        string_match = f"{raingaugereading.device_id}__{raingaugereading.datetime}"
        self.assertEqual(str(raingaugereading), string_match)

    def test_tankmonitorreading_string(self):
        """Test tank monitor reading model returns a string"""
        user = sample_user()
        aloc = models.Location.objects.create(
            loc_id=12345,
            loc_name='Johnson Farm',
            user=user
        )
        adevicetype = models.Devicetype.objects.create(
            device_type='Soil Moisture Probe'
        )
        adevice = models.Device.objects.create(
            device_id=11123,
            device_type=adevicetype,
            user=user
        )
        tankmonreading = models.Tankmonitorreading.objects.create(
            user=user,
            loc=aloc,
            device=adevice,
            datetime="2020-06-01T21:10:24.000Z",
            water_height_mm=34.2,
            rainfall_mm=13.0,
        )
        string_match = f"{tankmonreading.device}__{tankmonreading.datetime}"
        self.assertEqual(str(tankmonreading), string_match)
