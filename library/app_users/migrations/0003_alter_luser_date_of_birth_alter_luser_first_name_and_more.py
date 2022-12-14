# Generated by Django 4.1.4 on 2022-12-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_luser_library_card_number_alter_luser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='luser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='luser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
