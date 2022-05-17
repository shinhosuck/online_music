from django.contrib import admin
from music.models import (
    Genre, 
    Album,
    Like,
    Dislike,
    RecentlyPlayed,
    Song
)


admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(RecentlyPlayed)
admin.site.register(Song)

