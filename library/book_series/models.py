from cloudinary.models import CloudinaryField
import cloudinary.uploader
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import random
from library.author.models import Author


class BookSeries(models.Model):
    name = models.CharField(max_length=100)
    author = models.ManyToManyField(Author, related_name="series_author")
    image = CloudinaryField('image', blank=True, null=True)
    slug = models.SlugField(max_length=100, editable=False, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(f"{self.name}-{random.randint(1, 101)}")
        super(BookSeries, self).save(*args, **kwargs)


@receiver(pre_delete, sender=BookSeries)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
