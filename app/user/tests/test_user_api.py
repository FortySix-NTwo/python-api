from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse("user:create")
AUTH_TOKEN_URL = reverse("user:token")


def create_user(**params):
    """Create New User API Request"""
    return get_user_model().objects.create_user(**params)


class UserApiTest(TestCase):
    """Test the users API non authenticated"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user(self):
        """Test User Creation with Valid Payload is Successful"""
        payload = {
            "email": "test@which.com",
            "password": "passTheTest",
            "name": "test user",
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)

        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_exists(self):
        """Test Creation of already existing user"""
        payload = {
            "email": "test@where.com",
            "password": "passTheTest",
            "name": "test user",
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_under_eight_chars(self):
        """Test if Password is less then 8 elements"""
        payload = {"email": "test@whoami.com", "password": "pass", "name": "test user"}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEquals(res.status_code, status.HTTP_400_BAD_REQUEST)

        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()

        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test token creation per user creation request"""
        payload = {"email": "test@which.com", "password": "passTheTest"}
        create_user(**payload)
        res = self.client.post(AUTH_TOKEN_URL, payload)

        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that bad requests are processed correctly"""
        create_user(email="test@tests.com", password="testpass")
        payload = {"email": "test@tests.com", "password": "wrongpass"}
        res = self.client.post(AUTH_TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that invalid requests are processed correctly"""
        payload = {"email": "test@tests.com", "password": "testpass"}
        res = self.client.post(AUTH_TOKEN_URL, payload)

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_fieldO(self):
        """Test that bad and missing fields requests are processed correctly"""
        res = self.client.post(AUTH_TOKEN_URL, {"email": "email", "password": ""})

        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
