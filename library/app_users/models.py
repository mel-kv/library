from datetime import date

import random
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from django.utils.translation import gettext_lazy as _

from library.app_users.managers import CustomUserManager


class LUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30, )
    last_name = models.CharField(max_length=30, )
    date_of_birth = models.DateField(default='1990-01-01')
    updated = models.DateField(auto_now=True)
    # library_card_number = models.SmallIntegerField(editable=False, blank=True, null=True, max_length=10)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, )
    slug = models.SlugField(max_length=55, editable=False, blank=False, null=False, unique=True)


    objects = CustomUserManager()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.full_name} - {self.is_staff} ({self.calculate_age})'

    @property
    def calculate_age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - \
               ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(f"{self.full_name}-{random.randint(1, 101)}")
        super(LUser, self).save(*args, **kwargs)
