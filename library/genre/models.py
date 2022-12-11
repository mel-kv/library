from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import random


class Genre(models.Model):
    TYPES = (
        ('Fantasy', 'Fantasy'),
        ('Historical fiction', 'Historical fiction'),
        ('Short stories', 'Short stories'),
        ('Poetry', 'Poetry'),
        ('Thrillers', 'Thrillers'),
        ('War', 'War'),
        ('Women’s fiction', 'Women’s fiction'),
        ('Fairy tales, fables, and folk tales', 'Fairy tales, fables, and folk tales'),
        ('Crime', 'Crime'),
        ('Plays', 'Plays'),
        ('Young adult', 'Young adult'),
        ('Romance', 'Romance'),
        ('Classics', 'Classics'),
        ('Humour and satire', 'Humour and satire'),
        ('Horror', 'Horror'), ('Mystery', 'Mystery'),
        ('Science fiction', 'Science fiction'),
        ('Literary fiction', 'Literary fiction'),
        ('Adventure stories', 'Adventure stories'),
        ('Autobiography and memoir', 'Autobiography and memoir'),
        ('Biography', 'Biography'),
        ('Essays', 'Essays'),
        ('Non-fiction novel', 'Non-fiction novel'),
        ('Self-help', 'Self-help'),

    )
    type = models.CharField(max_length=40, choices=TYPES)
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


