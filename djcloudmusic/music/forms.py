from music.models import Album, Song
from django import forms


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "choose_genre", "create_genre", "album_cover"]


class CreateSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ["title", "song_file", "file_type", ]
