# Generated by Django 4.1.4 on 2022-12-17 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0001_initial'),
        ('book_series', '0003_bookseries_books_in_series'),
        ('book', '0006_alter_book_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='book_publisher', to='publisher.publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='book_series', to='book_series.bookseries'),
        ),
    ]
