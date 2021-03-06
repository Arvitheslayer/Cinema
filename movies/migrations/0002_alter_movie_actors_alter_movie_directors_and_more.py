# Generated by Django 4.0.2 on 2022-05-05 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='actors'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.ManyToManyField(related_name='film_director', to='movies.Actor', verbose_name='director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='geners',
            field=models.ManyToManyField(to='movies.Genre', verbose_name='genres'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='film'),
        ),
    ]
