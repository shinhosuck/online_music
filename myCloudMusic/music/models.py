from re import T
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils import timezone
# from PIL import Image


class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    choose_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    create_genre = models.CharField(max_length=20, null=True, blank=True)
    album_cover = models.ImageField(default="album_img/default.jpg", upload_to="album_img", blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)


    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    song_file = models.FileField(upload_to="songs", blank=True)
    file_type = models.CharField(max_length=10)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ManyToManyField(User, related_name="likes", blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.album.title

class Dislike(models.Model):
    user = models.ManyToManyField(User, related_name="dislikes", blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.album.title


class RecentlyPlayed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date_created"]
        verbose_name_plural = "Recently played"

    def __str__(self):
        return self.album.title