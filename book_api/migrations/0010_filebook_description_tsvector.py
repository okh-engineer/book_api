# Generated by Django 4.0 on 2023-07-14 16:31

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0009_remove_audiobook_category_remove_audiobook_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filebook',
            name='description_tsvector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]