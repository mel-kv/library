import random
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, editable=True, blank=True, null=True)
    description = models.TextField()
    year_founded = models.SmallIntegerField(
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(f"{self.name}-{random.randint(1, 101)}")
        super(Publisher, self).save(*args, **kwargs)