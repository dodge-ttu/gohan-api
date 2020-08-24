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
        """Test that the auth token is required to access the endpoint"""
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
        self.client.force_authenticate(self.user)

    def test_retrieve_raingaugereadings_list(self):
        """Test retrieving a list of rain gauge readings"""
        aloc = models.Location.objects.create(
            loc_id=12345,
            loc_name='Johnson Farm',
            user=self.user
        )
        adevicetype = models.Devicetype.objects.create(
            device_type='Soil Moisture Probe'
        )
        adevice = models.Device.objects.create(
            device_id=11123,
            device_type=adevicetype,
            user=self.user
        )
        models.Raingaugereading.objects.create(
            LocationID=aloc,
            LocationDescription=aloc.loc_name,
            deviceID=adevice,
            SystemType='Metric',
            datetime="2020-06-01T21:10:24.000Z",
            rain=0.2,
            AccumulatedRain=45.6,
        )
        models.Raingaugereading.objects.create(
            LocationID=aloc,
            LocationDescription=aloc.loc_name,
            deviceID=adevice,
            SystemType='Metric',
            datetime="2020-06-01T21:11:24.000Z",
            rain=1.2,
            AccumulatedRain=17.6,
        )
        res = self.client.get(RAINGAUGEREADING_URL)
        readings = models.Raingaugereading.objects.all()
        serializer = RaingaugereadingSerializer(readings, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
