from django.urls import path 
from music.views import (
    all_albums,
    home,
    like,
    dislike,
    landing_page,
    create_album,
    create_song,
    all_albums,
    play_album
)

app_name = "music"

urlpatterns = [
    path("", landing_page, name="landing-page"),
    path("home", home, name="home"),
    path("album/<int:pk>/like", like, name="like"),
    path("album/<int:pk>/dislike", dislike, name="dislike"),
    path("create/new/album", create_album, name="create-album"),
    path("create/new/song/", create_song, name="create-song"),
    path("all/<string>", all_albums, name="all-albums"),
    path("play/album/<int:pk>", play_album, name="play-album"),
]