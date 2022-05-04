from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField('Category', max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='actors/')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField('Name', max_length=100)
    tagline = models.CharField('Tagline', max_length=100, default='')
    description = models.TextField('Description')
    poster = models.ImageField('Poster', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Release date', default=2019)
    country = models.CharField('Country', max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name='director', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='actors', related_name='film_actor')
    geners = models.ManyToManyField(Genre, verbose_name='genres')
    world_premiere = models.DateField('World premiere', default=date.today)
    budget = models.PositiveIntegerField('Budget', default=0, help_text='enter the amount in dollars')
    fees_in_usa = models.PositiveIntegerField('US fees', default=0, help_text='enter the amount in dollars')
    fees_in_world = models.PositiveIntegerField('World fees', default=0, help_text='enter the amount in dollars')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title


class MovieShots(models.Model):
    title = models.CharField('Name', max_length=100)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Film', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    value = models.SmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value


class Rating(models.Model):
    ip = models.CharField('IP', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='star')
    movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name='film')

    def __str__(self):
        return f'(self.star) - (self.movie)'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=100)
    text = models.TextField("Message", max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Parent', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='film', on_delete=models.CASCADE)

    def __str__(self):
        return f'(self.name) - (self.movie)'