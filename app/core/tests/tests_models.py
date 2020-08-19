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

    def test_device_string(self):
        """Test the device string representation"""
        device = models.Device.objects.create(
            user=sample_user(),
            device_type='Soil Moisture Probe'
        )

        self.assertEqual(str(device), device.device_type)

    def test_location_string(self):
        """Test the location string representation"""
        location = models.Location.objects.create(
            user=sample_user(),
            loc_id='23111',
            loc_name='Dodge low water',
        )
        self.assertEqual(str(location), location.loc_name)
