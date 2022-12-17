# Generated by Django 4.1.4 on 2022-12-17 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0007_alter_book_publisher_alter_book_series_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='reader',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='book_checkedout', to=settings.AUTH_USER_MODEL),
        ),
    ]
