# Generated by Django 4.0.4 on 2022-05-04 18:54

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Age')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Image')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Tagline')),
                ('description', models.TextField(verbose_name='Description')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default=2019, verbose_name='Release date')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='World premiere')),
                ('budget', models.PositiveIntegerField(default=0, help_text='enter the amount in dollars', verbose_name='Budget')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='enter the amount in dollars', verbose_name='US fees')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='enter the amount in dollars', verbose_name='World fees')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movies.actor', verbose_name='actors')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.category', verbose_name='Category')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movies.actor', verbose_name='director')),
                ('geners', models.ManyToManyField(to='movies.genre', verbose_name='genres')),
            ],
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Value')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('text', models.TextField(max_length=5000, verbose_name='Message')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='film')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.reviews', verbose_name='Parent')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movies.movie', verbose_name='film')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.ratingstar', verbose_name='star')),
            ],
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Image')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Film')),
            ],
        ),
    ]