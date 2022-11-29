from django.urls import path 
from music.views import (
    all_albums,
    home,
    like,
    dislike,
    landing_page,
    create_album,
    new_song,
    add_song,
    all_albums,
    my_albums,
    play_album,
    genre,
    genre_albums,
    my_albums,
    about_us,
    contact_us,
    home_header_genres
)

app_name = "music"

urlpatterns = [
    path("", landing_page, name="landing-page"),
    path("home", home, name="home"),
    path("album/<int:pk>/like", like, name="like"),
    path("album/<int:pk>/dislike", dislike, name="dislike"),
    path("create/new/album", create_album, name="create-album"),
    path("create/new/song/", new_song, name="new-song"),
    path("album/<int:pk>/add/song", add_song, name="add-song"),
    path("all/<string>", all_albums, name="all-albums"),
    path("play/album/<int:pk>", play_album, name="play-album"),
    path("playlist/genres", genre, name="genre"),
    path("playlist", genre_albums, name="genre-albums"),
    path("my/albums", my_albums, name="my-albums"),
    path("about/us", about_us, name="about-us"),
    path("contact/us", contact_us, name="contact-us"),
    path("view/by/genres", home_header_genres, name="home-header-genres")
]
