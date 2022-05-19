from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
# Create your models here.
class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        username_attr = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{username_attr: username})

class User(AbstractUser):
    email_confirmed = models.BooleanField(default=False)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initial_email = self.email

    def save(self, *args, **kwargs):
        if self.email != self._initial_email:
            self.email_confirmed = False
        super().save(*args, **kwargs)

    objects = CustomUserManager()

MEMBERSHIP_TYPES = (
    ("lender", "Lender"),
    ("borrower", "Borrower"),
    ("lender_and_borrower", "Lender & Borrower")
)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200, unique=True)
    phone_number = PhoneNumberField(unique=True)
    membership = models.CharField(max_length=200, choices=MEMBERSHIP_TYPES)
    postal_code = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
