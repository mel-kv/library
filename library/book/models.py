from cloudinary.models import CloudinaryField
import cloudinary.uploader
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
import random

from library.author.models import Author
# from library.book_series.models import BookSeries
from library.genre.models import Genre
from library.publisher.models import Publisher
from django.urls import reverse


class AvailableBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Book.Status.AVAILABLE)


class Book(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'IN', 'On the shelf'
        TAKEN = 'OUT', 'Checked Out'
        RESERVED = 'RES', 'Reserved'

    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    author = models.ManyToManyField(Author, related_name="book_author")
    genres = models.ManyToManyField(Genre, related_name="book_genre")
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, related_name="book_publisher")
    isbn = models.PositiveIntegerField(unique=True, editable=False)
    pages = models.SmallIntegerField()
    series = models.BooleanField()
    # series_name = models.ForeignKey(BookSeries, on_delete=models.DO_NOTHING, related_name="book_series", null=True,
    #                                 blank=True)
    release_number_of_series = models.SmallIntegerField(null=True, blank=True)
    originally_published = models.DateField()
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.AVAILABLE)
    description = models.TextField()
    slug = models.SlugField(max_length=100, editable=False, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    objects = models.Manager()
    available = AvailableBookManager()

    def __str__(self):
        return f'{self.title} ({self.author})'

    class Meta:
        ordering = ['title', 'status']
        indexes = [
            models.Index(fields=['-updated'])
        ]

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(f"{self.title}-{random.randint(1, 101)}")
        super(Book, self).save(*args, **kwargs)


def generate_unique_isbn():
    isbn_candidate = random.randint(1000000000, 2147483647)
    if Book.objects.filter(isbn__exact=isbn_candidate):
        generate_unique_isbn()
    else:
        return isbn_candidate


@receiver(pre_save, sender=Book)
def generate_isbn(sender, instance, **kwargs):
    instance.isbn = generate_unique_isbn()


@receiver(pre_delete, sender=Book)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
