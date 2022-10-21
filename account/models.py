from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        if not email:
            return ValueError('The given email must be set!')
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have status is_staff=True!')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have status is_superuser=True!')
        return self._create_user(email, password, **kwargs)


class Account(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField('email address', unique=True)
    name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.SmallIntegerField(blank=True, null=True)
    activation_code = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(_('active'),
                                    default=False,
                                    help_text=_(
                                        'Designates whether this user should be treted as active.'
                                        'Unselect this instead of deleting accounts.'
                                    ))

    created_at = models.DateTimeField

    objects = UserManager()

    def __str__(self):
        return self.username

    def create_activation_code(self):
        import uuid
        code = str(uuid.uuid4())
        self.activation_code = code
