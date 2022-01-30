from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('movies/', views.movie_listing, name='movie-list'),
    path('movies/<int:movie_id>/', views.movie_description, name='about-movie'),
    path('movies/movies/', views.add_comment, name='add_comment'),
    #path('movies/search/', views.movie_search, name='movie-search'),
]
