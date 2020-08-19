from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Device

from devices.serializers import DeviceSerializer

DEVICE_URL = reverse('devices:device-list')


class PublicTagApiTests(TestCase):
    """Test the publicly avialable tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving tags"""
        res = self.client.get(DEVICE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagApiTests(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@iamdodge.us',
            'TestPass123'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_device_tags(self):
        """Test retrieving device tags"""
        Device.objects.create(user=self.user, device_type='Weather Station')
        Device.objects.create(user=self.user, device_type='Soil Moisture Probe')

        res = self.client.get(DEVICE_URL)
        tags = Device.objects.all().order_by('-device_type')
        serializer = DeviceSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test tags are for authenticated user"""
        user2 = get_user_model().objects.create_user(
            'other@iamdodge.us',
            'PassTest456'
        )
        Device.objects.create(user=user2, device_type='Rain Guage')
        tag = Device.objects.create(user=self.user, device_type='Tank Monitor')

        res = self.client.get(DEVICE_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['device_type'], tag.device_type)

    def test_create_tag_successful(self):
        """Test creating a new tag"""
        payload = {
            'device_type': 'Soil Moisture Probe',
        }
        self.client.post(DEVICE_URL, payload)
        exists = Device.objects.filter(
            user=self.user,
            device_type=payload['device_type']
        ).exists()
        self.assertTrue(exists)

    def test_create_invalid_tag(self):
        """Test creating an invalid tag fails"""
        payload = {
            'device_type': '',
        }
        res = self.client.post(DEVICE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
