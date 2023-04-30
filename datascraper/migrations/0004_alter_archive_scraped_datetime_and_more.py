# Generated by Django 4.2 on 2023-04-29 19:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datascraper', '0003_alter_archivetemplate_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='scraped_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 29, 22, 22, 29, 827061)),
        ),
        migrations.AlterField(
            model_name='forecast',
            name='scraped_datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 29, 22, 22, 29, 826471)),
        ),
    ]
