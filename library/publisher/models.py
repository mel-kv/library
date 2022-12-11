from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55, editable=True, unique=True,  blank=True, null=True)
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
