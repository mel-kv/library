# Generated by Django 4.1.4 on 2022-12-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='type',
            field=models.CharField(max_length=40),
        ),
    ]
