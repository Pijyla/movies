from django.contrib import admin
from .models import Movie, Comment

class MovieAdmin(admin.ModelAdmin):
    """Customize the look of the auto-generated admin for the Movie model"""
    list_display = ('movie', 'year', 'category', 'IMDb_rating')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Comment)
