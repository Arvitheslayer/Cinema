# Generated by Django 4.0.2 on 2022-11-21 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_actors_alter_movie_directors_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'verbose_name': 'Actor', 'verbose_name_plural': 'Actors'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Genre', 'verbose_name_plural': 'Genres'},
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'Movie', 'verbose_name_plural': 'Movies'},
        ),
        migrations.AlterModelOptions(
            name='movieshots',
            options={'verbose_name': 'Movie shot', 'verbose_name_plural': 'Movie shots'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Rating', 'verbose_name_plural': 'Ratings'},
        ),
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'verbose_name': 'Rating star', 'verbose_name_plural': 'Rating stars'},
        ),
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
    ]
