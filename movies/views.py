from django.shortcuts import render
from .models import Movie
from .forms import CommentForm

def movie_listing(request):
    """A view of all movies."""
    movies = Movie.objects.all() # SELECT * FROM MOVIE
    return render(request, 'movies/movie_listing.html', {'movies': movies})

def movie_description(request, movie_id):
    """A view of movie details."""
    movie = Movie.objects.get(pk=movie_id) # SELECT * FROM MOVIE WHERE ID = movie_id
    return render(request, 'movies/movie_description.html', {'movie': movie})

def homepage(request):
    movies = Movie.objects.all() # SELECT * FROM MOVIE
    return render(request, 'movies/homepage.html', {'movies': movies})

def add_comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'movies/add_comment.html', {'form': form})
