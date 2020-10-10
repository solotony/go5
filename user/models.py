from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True


    def _create_user(self, email, phone, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email and not phone:
            raise ValueError(_('Even one of Email or Phone should have a value.'))
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_user(self, email, phone, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone, password, **extra_fields)


    def create_superuser(self, email, phone, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(email, phone, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    username = None

    # changes email to unique and blank to false
    email = models.EmailField(
        _('Email address'),
        blank=True,
        null=True,
        unique=True
    )

    phone = PhoneNumberField(
        _('Phone number'),
        blank=True,
        null=True,
        unique=True
    )

    patronymic_name = models.CharField(
        _('patronymic name'),
        max_length=30,
        blank=True
    )

    USERNAME_FIELD = 'phone'

    def clean(self):
        super().clean()
        if not self.email and not self.phone:
            raise ValidationError({'phone': _('Even one of Email or Phone should have a value.')})


    def __str__(self):
        return self.get_printable_name()

    def get_name(self):
        name = ''
        if self.last_name:
            name = self.last_name
        if self.first_name:
            if name:
                name += ' '
            name  += self.first_name
            if self.patronymic_name:
                if name:
                    name += ' '
                name += self.patronymic_name
        if name:
            return name
        return ''

    def get_printable_name(self):
        name = self.get_name()
        if name:
            return name
        if self.phone:
            return str(self.phone)
        return self.email


