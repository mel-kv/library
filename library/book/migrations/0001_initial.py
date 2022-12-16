# Generated by Django 4.1.4 on 2022-12-16 17:25

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
        ('author', '0001_initial'),
        ('publisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('isbn', models.PositiveIntegerField(editable=False, unique=True)),
                ('pages', models.SmallIntegerField()),
                ('series', models.BooleanField()),
                ('release_number_of_series', models.SmallIntegerField(blank=True, null=True)),
                ('originally_published', models.DateField()),
                ('status', models.CharField(choices=[('IN', 'On the shelf'), ('OUT', 'Checked Out'), ('RES', 'Reserved')], default='IN', max_length=3)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('author', models.ManyToManyField(related_name='book_author', to='author.author')),
                ('genres', models.ManyToManyField(related_name='book_genre', to='genre.genre')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='book_publisher', to='publisher.publisher')),
            ],
            options={
                'ordering': ['title', 'status'],
            },
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['-updated'], name='book_book_updated_65d032_idx'),
        ),
    ]
