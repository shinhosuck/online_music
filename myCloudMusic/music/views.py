import re
from django.contrib.auth.decorators import login_required
from music.models import Album, Like, Dislike, RecentlyPlayed, Genre
from django.shortcuts import render, redirect
from music.forms import CreateAlbumForm, CreateSongForm


def landing_page(request):
    user = request.user
    print(user)
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
        print(new_genre)

        if form.is_valid():

            new_album = form.save()
            album = Album.objects.get(pk=new_album.id)
            print(album)
            if new_genre:
                add_genre = Genre.objects.create(genre=new_genre)
                album.choose_genre = add_genre
                print(add_genre.id)
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
        print(most_listened)
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
    album = Album.objects.get(pk=pk)
    user = request.user

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

    context = {
        "album": album
    }
    return render(request, "music/play_album.html", context)


@login_required
def create_song(request):
    # if request.method == "POST":
    #     form = CreateSongForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("music:home")
    # else:
    #     form = CreateSongForm()
    #     context = {
    #         "form": form
    #     }
    #     return render(request, "music/create_song.html", context)
    user = request.user
    albums = user.album_set.all()
    context = {
        "albums": albums
    }
    return render(request, "music/my_albums.html", context)


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
        genre = request.GET.get("string")
        genre_albums = ''
        albums = Album.objects.all()
        for album in albums:
            if album.genre.genre == genre:
                genre_albums = album.genre.album_set.all()
        context = {
            "genre": genre,
            "genre_albums": genre_albums
        }
    return render(request, "music/all_genre_albums.html", context)