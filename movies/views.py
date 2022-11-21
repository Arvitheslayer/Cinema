from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Movie

class MoviesView(ListView):
    '''list of films'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movie_list.html'

class MovieDetailView(DetailView):
    '''full description of film'''
    model = Movie
    slug_field = 'url'