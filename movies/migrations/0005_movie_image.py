# Generated by Django 4.0.1 on 2022-01-29 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_rename_imbd_rating_movie_imdb_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.URLField(default='', max_length=250),
        ),
    ]
