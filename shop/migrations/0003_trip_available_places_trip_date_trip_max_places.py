# Generated by Django 5.0.3 on 2024-06-26 19:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_trip_options_option_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='available_places',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='trip',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trip',
            name='max_places',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
