# Generated by Django 4.1.4 on 2022-12-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_series', '0002_bookseries_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookseries',
            name='books_in_series',
            field=models.PositiveIntegerField(default=7),
            preserve_default=False,
        ),
    ]
