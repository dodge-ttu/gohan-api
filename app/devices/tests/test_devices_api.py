from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Devicetag

from devices.serializers import DevicetagSerializer

DEVICETAGS_URL = reverse('devices:devicetag-list')


class PublicTagApiTests(TestCase):
    """Test the publicly avialable tags API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving tags"""
        res = self.client.get(DEVICETAGS_URL)

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
        Devicetag.objects.create(user=self.user, name='Weather Station')
        Devicetag.objects.create(user=self.user, name='Soil Moisture Probe')

        res = self.client.get(DEVICETAGS_URL)
        tags = Devicetag.objects.all().order_by('-name')
        serializer = DevicetagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test tags are for authenticated user"""
        user2 = get_user_model().objects.create_user(
            'other@iamdodge.us',
            'PassTest456'
        )
        Devicetag.objects.create(user=user2, name='Rain Guage')
        tag = Devicetag.objects.create(user=self.user, name='Tank Monitor')

        res = self.client.get(DEVICETAGS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

    def test_create_tag_successful(self):
        """Test creating a new tag"""
        payload = {
            'name': 'Soil Moisture Probe',
        }
        self.client.post(DEVICETAGS_URL, payload)
        exists = Devicetag.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_invalid_tag(self):
        """Test creating an invalid tag fails"""
        payload = {
            'name': '',
        }
        res = self.client.post(DEVICETAGS_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
