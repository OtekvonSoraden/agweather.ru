# Generated by Django 4.2.4 on 2023-12-16 11:45

import datascraper.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0029_alter_forecasttemplate_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivetemplate',
            name='url',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='forecasttemplate',
            name='url',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]*$', 'Only roman characters are allowed.'), datascraper.models.validate_first_upper]),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]*$', 'Only roman characters are allowed.'), datascraper.models.validate_first_upper]),
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9 ]*$', 'Only roman characters are allowed.'), datascraper.models.validate_first_upper]),
        ),
    ]