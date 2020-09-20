import os
import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


def user_image_file_path(instance, filename):
    """Generate file path for user image upload"""
    extension = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{extension}"

    return os.path.join("uploads/user/", filename)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates & Save a new User"""

        if not email:
            raise ValueError("Users must include a valid email address")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates Administrative User"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model Supporting Email instead of Username"""

    avatar = models.ImageField(null=True, upload_to=user_image_file_path)
    name = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = "email"
