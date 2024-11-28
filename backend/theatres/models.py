from django.db import models
from movies.models import Movie
from .validators import validate_showtime_overlap
# Create your models here.

class Theatre(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Screen(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="screens")
    screen_number = models.CharField(max_length=10)
    seat_capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.theatre.name} - Screen {self.screen_number}"
    

class Seat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name="seats")
    row = models.CharField(max_length=5)
    number = models.PositiveIntegerField()
    is_vip = models.BooleanField(default=False)

    class Meta:
        unique_together = ("screen", "row", "number")

    def __str__(self):
        return f"Seat {self.row}{self.number} in {self.screen}"

class ShowTime(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name="showtimes")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="showtimes")
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        unique_together = ("screen", "movie", "date", "time")
    
    def clean(self):
        validate_showtime_overlap(self)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.movie.title} - {self.screen.theatre.name} {self.screen} at {self.time} on {self.date}"
