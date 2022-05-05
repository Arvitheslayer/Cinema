from django.shortcuts import render

from .models import movie

class MoviesView(Views):
    '''list of films'''
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/movie_list.html', {'movie_list':movies})
