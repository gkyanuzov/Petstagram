from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from Petstagram2.accounts.managers import PetstagramUserManager
from Petstagram2.main.validators import only_letters_validator

""""
1.Create model extending
2.Configure this model in settings.py
3.Create user manager
"""


class PetstagramUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENTGH = 25
    username = models.CharField(
        max_length=USERNAME_MAX_LENTGH,
        unique=True,
    )

    date_joind = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()

class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2

    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            only_letters_validator,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    decsription = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        PetstagramUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
