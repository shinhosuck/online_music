from django.contrib.auth.decorators import login_required
from music.models import Album, Like, Dislike, RecentlyPlayed, Genre, Song
from django.shortcuts import render, redirect
from music.forms import CreateAlbumForm, CreateSongForm
from mutagen.mp3 import MP3
import math
import platform


def landing_page(request):
    return render(request, "music/landing_page.html", {})


def home(request):
    user = request.user
    albums = Album.objects.all()
    most_listened = albums
    latest_albums = albums[0:8]
    you_might_also_like = Album.objects.all()[0:8]
    
    if not user.is_authenticated:
        context = {
            "latest_albums": latest_albums,
            "most_listened": most_listened,
            "you_might_also_like": you_might_also_like
        }
        return render(request, "music/home.html", context)

    recently_played = user.recentlyplayed_set.all()[0:8]
    context = {
        "latest_albums": latest_albums,
        "recently_played": recently_played,
        "most_listened": most_listened,
        "you_might_also_like": you_might_also_like
    }
    return render(request, "music/home.html", context)



@login_required
def like(request, pk):
    album = Album.objects.get(pk=pk)
    dislike_album = album.dislike_set.filter(album=album).first()
    user = request.user

    try:
        if not album.like_set.get(album=album):
            pass
    except:
        new_like_album = Like.objects.create(album=album)
        new_like_album.user.add(user)

    if user not in album.like_set.get(album=album).user.all():
        like_album = album.like_set.get(album=album)
        like_album.user.add(user)

    if not dislike_album:
        pass
    else:
        album.dislike_set.get(album=album).user.remove(user)
        album.thumbs_down = album.dislike_set.get(album=album).user.all().count()

    like_album = album.like_set.get(album=album)
    album.thumbs_up = like_album.user.all().count()
    album.save()
    return redirect("music:play-album", pk=pk)


@login_required
def dislike(request, pk):
    album = Album.objects.get(pk=pk)
    like_album = album.like_set.filter(album=album).first()
    user = request.user

    try:
        if not album.dislike_set.get(album=album):
            pass
    except:
        new_dislike_album = Dislike.objects.create(album=album)
        new_dislike_album.user.add(user)

    if user not in album.dislike_set.get(album=album).user.all():
        dislike_album = album.dislike_set.get(album=album)
        dislike_album.user.add(user)

    if not like_album:
        pass
    else:
        album.like_set.get(album=album).user.remove(user)
        album.thumbs_up = album.like_set.get(album=album).user.all().count()

    dislike_album = album.dislike_set.get(album=album)
    album.thumbs_down =  dislike_album.user.all().count()
    album.save()
    return redirect("music:play-album", pk=pk)


@login_required
def create_album(request):
    user = request.user
    if request.method == "POST":
        form = CreateAlbumForm(request.POST, request.FILES)
        form.instance.user = user 
        new_genre = form["create_genre"].value()
        if form.is_valid():
            new_album = form.save()
            album = Album.objects.get(pk=new_album.id)
            if new_genre:
                add_genre = Genre.objects.create(genre=new_genre)
                album.choose_genre = add_genre
            album.save()
            return redirect("music:home")
    else:
        form = CreateAlbumForm() 
        context = {
            "form": form
        }
    return render(request, "music/create_album.html", context)


def all_albums(request, string):
    user = request.user
    if string == "recently played" and user.is_authenticated:
        recently_played = user.recentlyplayed_set.all()
        context = {
        "recently_played": recently_played,
        "string": string
        }
        return render(request, "music/all_albums.html", context)
    
    if string == "latest albums":
        latest_albums = Album.objects.all()[0:16]
        context = {
            "latest_albums": latest_albums,
            "string": string
        }
        return render(request, "music/all_albums.html", context)
    
    if string == "most listened":
        most_listened = Album.objects.filter(thumbs_up=1)
        context = {
            "most_listened": most_listened,
            "string": string
        }
        return render(request, "music/all_albums.html", context)

    if string == "you might also like":
        you_might_also_like = Album.objects.all()
        context = {
            "you_might_also_like": you_might_also_like,
            "string": string
        }
        return render(request, "music/all_albums.html", context)

def play_album(request, pk):
    operating_system = platform.platform()
    new = operating_system.split("-")

    user = request.user
    album = Album.objects.get(pk=pk)

    song_length = []
    int_min_sec = {}
    songs = album.song_set.all()

    for song in songs:
        audio = MP3(song.song_file)
        audio_length = audio.info.length
        minute = str(math.trunc((audio_length % 3600) / 60))

        # Integer minute
        int_min = math.trunc((audio_length % 3600) / 60)
        # end

        second = str(math.trunc(audio_length % 60))

        # Integer second
        int_sec = math.trunc(audio_length % 60)
        # end

        print(f"{int_min}:{int_sec}")
        
       
        if len(second) == 1:
            song_length.append(f"{minute}:0{second}")
        elif len(second) < 1:
            song_length.append(f"{minute}:00{second}")
        elif len(minute) < 1:
            song_length.append(f"0{minute}:{second}")
        else:
            song_length.append(f"{minute}:{second}")
    
    # delete old recenttly played and create new one
    if user.is_authenticated:
        albums = user.recentlyplayed_set.all()
        if albums:
            for recent_album in albums:
                if recent_album.album.pk == pk:
                    old_album = user.recentlyplayed_set.filter(album=album).first()
                    old_album.delete()
        RecentlyPlayed.objects.create(user=user, album=album)
    # end of delete and create recently played

    song_files = []
    songs = album.song_set.all()
    for song in songs:
        song_files.append(song.song_file)
    context = {
        "album": album,
        "songs": songs,
        "song_files": song_files,
        "song_length": song_length,
        "new": new
    }
    return render(request, "music/play_album.html", context)


@login_required
def new_song(request):
    user = request.user
    albums = user.album_set.all()
    context = {
        "albums": albums
    }
    return render(request, "music/my_albums.html", context)


def add_song(request, pk):
    user = request.user
    albums = user.album_set.all()
    if request.method == "POST":
        form = CreateSongForm(request.POST, request.FILES)
        if form.is_valid():
            album = Album.objects.get(pk=pk)
            form.instance.album = album
            form.save()
        return redirect("music:new-song")
    else:
        form = CreateSongForm()
        context = {
            "form": form
        }
        return render(request, "music/add_song_form.html", context)
    
@login_required
def my_albums(request):
    user = request.user
    albums = user.album_set.all()
    if request.GET.get("string"):
        data = request.GET.get("string")
        context = {
            "data": data,
            "albums": albums
        }
        return render(request, "music/my_albums.html", context)


def genre(request):
    genres = Genre.objects.all()
    context = {
        "genres": genres
    }
    return render(request, "music/genres.html", context)


def genre_albums(request):
    if request.GET.get("string"):
        genre_atring = request.GET.get("string")
        genre = Genre.objects.filter(genre=genre_atring).first()
        genre_albums = genre.album_set.all()
        context = {
            "genre": genre,
            "genre_albums": genre_albums
        }
    return render(request, "music/all_genre_albums.html", context)
