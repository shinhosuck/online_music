from django.shortcuts import render, redirect
from users.forms import UserRegisterForm, MessageForm
from users.models import UserProfile


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        # user = form.instance.username
        # print(user)
        if form.is_valid():
            user_form = form.save()
            print(user_form.username)
            return redirect("users:login")
    else:
         form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def message(request):
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            new_message = form.save()
            print(form.instance.email)
            print(new_message.email, new_message.message)
            # messages.success(request, f"Thank you very much for the message. I will get back to you as soon as possible.")
            return redirect("music:home")
        else:
            # messages.warning(request, f"Message did not sent. Please try again!")
            return redirect("music:home")

def user_profile(request):
    return render(request, "users/profile.html", {})