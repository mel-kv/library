from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import random


class Genre(models.Model):

    type = models.CharField(max_length=40, )
    description = models.TextField()
    slug = models.SlugField(max_length=55, editable=True,  blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(f"{self.type}-{random.randint(1,101)}")
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.type


