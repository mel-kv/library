from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
import random

from library.author.models import Author
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
    photo = models.URLField()
    author = models.ManyToManyField(Author, related_name="book_author")
    genres = models.ManyToManyField(Genre, related_name="book_genre")
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING, related_name="book_publisher")
    isbn = models.IntegerField(unique=True,)
    pages = models.SmallIntegerField()
    series = models.BooleanField()
    release_number_of_series = models.SmallIntegerField(null=True, blank=True)
    originally_published = models.DateField()
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.AVAILABLE)
    description = models.TextField()
    slug = models.SlugField(max_length=100, editable=False,  blank=True, null=True)
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
            self.slug = slugify(f"{self.title}-{random.randint(1,101)}")
        super(Book, self).save(*args, **kwargs)