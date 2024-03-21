from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff") or not extra_fields.get("is_superuser"):
            raise ValueError("is_staff and is_superuser fields must be set to true")
        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField( max_length=70)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=70, unique =True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self) -> str:
        return self.email



class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    key = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        key_user = f'User: {self.user}'
        return key_user


# signal to create an api key whenever a new user is created
@receiver(post_save, sender=User)
def create_api_key(sender, instance, created, **kwargs):
    if created:
        APIKey.objects.create(user=instance)
