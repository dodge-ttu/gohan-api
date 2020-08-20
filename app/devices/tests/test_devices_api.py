from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Devicetype, Device
from devices.serializers import DeviceSerializer, DevicetypeSerializer


DEVICETYPE_URL = reverse('devices:devicetype-list')
DEVICE_URL = reverse('devices:device-list')


def sample_user(email='test@iamdodge.us', password='TestPass123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class PublicTagApiTests(TestCase):
    """Test the publicly avialable tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving tags"""
        res = self.client.get(DEVICETYPE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.user = sample_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_device_types(self):
        """Test retrieving device tags"""
        Devicetype.objects.create(device_type='Weather Station')
        Devicetype.objects.create(device_type='Soil Moisture Probe')

        res = self.client.get(DEVICETYPE_URL)
        devtypes = Devicetype.objects.all().order_by('-device_type')
        serializer = DevicetypeSerializer(devtypes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_devices(self):
        """Test retrieving devices"""
        device_type = Devicetype.objects.create(device_type='Soil Moisture Probe')
        Device.objects.create(
            device_id=12345,
            device_type=device_type,
            user=self.user
        )
        Device.objects.create(
            device_id=1324,
            device_type=device_type,
            user=self.user
        )
        Device.objects.create(
            device_id=56743,
            device_type=device_type,
            user=self.user
        )
        res = self.client.get(DEVICE_URL)
        devices = Device.objects.all().order_by('-device_id')
        serializer = DeviceSerializer(devices, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_devices_limited_to_user(self):
        """Test tags are for authenticated user"""
        user2 = get_user_model().objects.create_user(
            'other@iamdodge.us',
            'PassTest456'
        )
        device_type = Devicetype.objects.create(device_type='Soil Moisture Probe')
        Device.objects.create(
            user=user2,
            device_id=1234,
            device_type=device_type
        )
        Device.objects.create(
            user=self.user,
            device_id=3456,
            device_type=device_type
        )

        res = self.client.get(DEVICE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_create_devicetype_successful(self):
        """Test creating a new device type"""
        payload = {
            'device_type': 'Soil Moisture Probe',
        }
        self.client.post(DEVICETYPE_URL, payload)
        exists = Devicetype.objects.filter(
            device_type=payload['device_type']
        ).exists()
        self.assertTrue(exists)

    def test_create_device_successful(self):
        """Test creating a new device"""
        payload = {
            'device_id': 12465,
            'device_type': 'Soil Moisture Probe',

        }
        self.client.post(DEVICE_URL, payload)
        exists = Device.objects.filter(
            user=self.user,
            device_id=payload['device_id'],
        ).exists()
        self.assertTrue(exists)

    def test_create_invalid_device_type(self):
        """Test creating an invalid device type fails"""
        payload = {
            'device_type': '',
        }
        res = self.client.post(DEVICETYPE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
