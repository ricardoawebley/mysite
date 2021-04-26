# Generated by Django 3.2 on 2021-04-26 22:57

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='title')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]
