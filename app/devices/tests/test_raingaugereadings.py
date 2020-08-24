from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core import models
from devices.serializers import RaingaugereadingSerializer

RAINGAUGEREADING_URL = reverse('devices:raingaugereading-list')


class PublicRaingaugereadingApiTests(TestCase):
    """Test the publibly available rain gauge readings API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test auth token is required to access the endpoint"""
        res = self.client.get(RAINGAUGEREADING_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRaingaugereadingApiTest(TestCase):
    """Test the private rain gauge readings API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@iamdodge.us',
            'TestPass123',
        )
        self.aloc = models.Location.objects.create(
            loc_id=11223,
            loc_name='Johnson Farm',
            user=self.user
        )
        self.device_type = models.Devicetype.objects.create(
            device_type='Soil Moisture Probe'
        )
        self.adevice = models.Device.objects.create(
            device_id=5467,
            device_type=self.device_type,
            user=self.user
        )
        self.client.force_authenticate(self.user)

    def create_rgr(self, **kwargs):
        """Create a rain gauge reading object"""
        rgr = models.Raingaugereading.objects.create(
            LocationID=kwargs.get('aloc', self.aloc),
            LocationDescription=self.aloc.loc_name,
            deviceID=kwargs.get('adevice', self.adevice),
            SystemType='Metric',
            datetime="2020-06-01T21:10:24.000Z",
            rain=0.2,
            AccumulatedRain=45.6,
        )
        return rgr

    def test_retrieve_raingaugereadings_list(self):
        """Test retrieving a list of rain gauge readings"""
        self.create_rgr()
        self.create_rgr()
        res = self.client.get(RAINGAUGEREADING_URL)
        readings = models.Raingaugereading.objects.all()
        serializer = RaingaugereadingSerializer(readings, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_rgr_limited_to_location(self):
        """Test rain gauge readings limited to location when provided"""
        aloc2 = models.Location.objects.create(
            loc_id=99999,
            loc_name='Tanner Farm',
            user=self.user
        )
        adevicetype2 = models.Devicetype.objects.create(
            device_type='Soil Moisture Probe'
        )
        adevice2 = models.Device.objects.create(
            device_id=1007,
            device_type=adevicetype2,
            user=self.user
        )

        rgr1 = self.create_rgr()
        self.create_rgr(aloc=aloc2, adevice=adevice2)
        res = self.client.get(RAINGAUGEREADING_URL, {'loc_id': 11223})
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['LocationID'], rgr1.LocationID.loc_id)
