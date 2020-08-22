from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Location

from devices.serializers import LocationSerializer

LOCATION_URL = reverse('devices:location-list')


class PublicLocationsApiTests(TestCase):
    """Test the publicly available ingredients API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_reqiured(self):
        """Test that the login is required to access the endpoint"""
        res = self.client.get(LOCATION_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateLocationsApiTest(TestCase):
    """Test the private locations API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@iamdodge.us',
            'TestPass123'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_locations_list(self):
        """Test retrieving a list of locations"""
        Location.objects.create(user=self.user,
                                loc_id=12345,
                                loc_name='Dodge low water')
        Location.objects.create(user=self.user,
                                loc_id=11223,
                                loc_name='Johnson Farm')

        res = self.client.get(LOCATION_URL)
        locations = Location.objects.all().order_by('-loc_name')
        serializer = LocationSerializer(locations, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_locations_limited_to_user(self):
        """Test locations for authenticated user are returned"""
        user2 = get_user_model().objects.create_user(
            'other@iamdodge.us',
            'PassTest321'
        )
        Location.objects.create(user=user2,
                                loc_id=12345,
                                loc_name='Dodge low water')

        location = Location.objects.create(user=self.user,
                                           loc_id=1223,
                                           loc_name='Johnson Farm')

        res = self.client.get(LOCATION_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['loc_name'], location.loc_name)

    def test_create_location_successful(self):
        """Test create a new location"""
        payload = {
            'user': self.user,
            'loc_id': 12345,
            'loc_name': 'Smith Farm',
        }
        self.client.post(LOCATION_URL, payload)
        exists = Location.objects.filter(
            user=self.user
        ).exists()
        self.assertTrue(exists)

    def test_create_location_invalid(self):
        """Test create a new location fails"""
        payload = {
            'loc_id': '',
            'loc_name': '',
        }
        res = self.client.post(LOCATION_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
