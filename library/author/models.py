import random
from django.db import models
from datetime import date

from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    photo = models.URLField()
    slug = models.SlugField(max_length=55, editable=True,  blank=True, null=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True, null=True)

    about_info = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)



    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    @property
    def calculate_age(self):
        today = date.today()
        if self.date_of_death:
            age = today.year - self.date_of_death.year - \
                   ((today.month, today.day) < (self.date_of_death.month, self.date_of_death.day))
        age = today.year - self.date_of_birth.year - \
              ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(f"{self.full_name}-{self.date_of_birth.year}")
        super(Author, self).save(*args, **kwargs)