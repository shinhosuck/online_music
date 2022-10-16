from shutil import unregister_archive_format
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, MessageForm, UserUpdateForm, ProfileUpdateForm
from users.models import Profile
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # user = form.instance.username
        # print(user)
        if form.is_valid():
            register_form = form.save()
            # print(user_form.username)
            messages.success(request, f"Successfully registered {register_form.username} !")
            return redirect("users:login")
    else:
         form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def message(request):
    user = request.user
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            new_message = form.save()
            if user.is_authenticated:
                messages.success(request, f"Message sent {user.username}!")
            else:
                messages.success(request, f"Message sent {new_message.email}!")
            return redirect("music:home")
        else:
            return redirect("music:home")

@login_required
def user_profile(request):
    user = request.user
    return render(request, "users/profile.html", {"user": user})

@login_required
def update_profile(request, pk):
    user = User.objects.get(pk=pk)
   
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST, request.FILES)
        return redirect("users:user-profile")

    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=user.profile)
        context = {
            "profile_form": profile_form,
            "user_form": user_form,
            "user": user
        }
        return render(request, "users/update_profile.html", context)
