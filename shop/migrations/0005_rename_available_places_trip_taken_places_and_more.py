# Generated by Django 5.0.3 on 2024-07-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_date_trip_end_date_remove_trip_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='available_places',
            new_name='taken_places',
        ),
        migrations.AlterField(
            model_name='trip',
            name='ig_link',
            field=models.URLField(default='https://stackoverflow.com/questions/46539714/select-all-occurrences-of-selected-word-in-vscode'),
        ),
    ]
