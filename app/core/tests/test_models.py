from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test Successful Creation of New User with Password Field"""
        email = "test@teasters.com"
        password = "SuperSecret"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalization(self):
        """Test The email Normalization Function"""
        email = "test@TESTERS.com"
        user = get_user_model().objects.create_user(email, "superSecret")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test User Creation Raises Error when Email Field is Undefined"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "superSecret")

    def test_create_new_superuser(self):
        """Test Creating new Users with Administrative Permissions"""
        user = get_user_model().objects.create_superuser("test@TesTers.com", "AdminPass")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
