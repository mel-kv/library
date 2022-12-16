from datetime import date
import random

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify

from django.utils.translation import gettext_lazy as _

from library.app_users.managers import CustomUserManager


class LUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    updated = models.DateField(auto_now=True)
    library_card_number = models.PositiveIntegerField(editable=False, unique=True, null=True, blank=True)

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
        if not self.library_card_number:
            self.library_card_number = generate_unique_library_card_number()
        super(LUser, self).save(*args, **kwargs)


def generate_unique_library_card_number():
    library_card_number_candidate = random.randint(1000000000, 2147483647)
    if LUser.objects.filter(library_card_number__exact=library_card_number_candidate):
        generate_unique_library_card_number()
    else:
        return library_card_number_candidate


@receiver(pre_save, sender=LUser)
def generate_unique_library_card(sender, instance, **kwargs):
    instance.unique_library_card = generate_unique_library_card_number()
