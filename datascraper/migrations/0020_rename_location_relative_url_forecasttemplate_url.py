# Generated by Django 4.2.4 on 2023-11-20 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0019_forecasttemplate_author_alter_location_country_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forecasttemplate',
            old_name='location_relative_url',
            new_name='url',
        ),
    ]
