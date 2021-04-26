# Generated by Django 3.2 on 2021-04-26 23:16

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='title'),
        ),
    ]