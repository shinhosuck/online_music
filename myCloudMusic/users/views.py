from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, MessageForm
from users.models import Profile
from django.contrib import messages


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
        # print(form.instance.email)
        if form.is_valid():
            new_message = form.save()
            # print(new_message.email, new_message.message)
            if user.is_authenticated:
                messages.success(request, f"Message sent {user.username}!")
            else:
                messages.success(request, f"Message sent {new_message.email}!")
            return redirect("music:home")
        else:
            return redirect("music:home")

def user_profile(request, pk):
    user = request.user
    if request.GET.get("string"):
        data = int(request.GET.get("string"))
        print(data)
        return redirect("users:user-profile", pk=pk)
    else:
        return render(request, "users/profile.html", {"user": user})
