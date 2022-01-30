from django.db import models

class Movie(models.Model):
    """A model of a movie."""
    movie = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=1000)
    category = models.CharField(choices=(
        ('act', 'Action'),
        ('ani', 'Animated'),
        ('adv', 'Adventurous'),
        ('bio', 'Biographical'),
        ('doc', 'Documentary'),
        ('dra', 'Drama'),
        ('san', 'Fantasy'),
        ('hor', 'Horror'),
        ('his', 'Historically'),
        ('com', 'Comedies'),
        ('cri', 'Crime'),
        ('mys', 'Mysteries'),
        ('mus', 'Music'),
        ('fam', 'Family'),
        ('war', 'War'),
        ('rom', 'Romantic'),
        ('sci', 'Sci-Fi'),
        ('spo', 'Sports'),
        ('thr', 'Thriller'),
        ('wes', 'Western'),
    ),
    max_length=3
)
    IMDb_rating = models.DecimalField(max_digits=2, decimal_places=1, default=1)
    image = models.URLField(max_length=250, default='')

    def __str__(self):
        return f'{self.movie}'

class Comment(models.Model):
    movie = models.ForeignKey(Movie, related_name="comments", on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.movie, self.user)
