from django.contrib.auth.views import LoginView, LogoutView
from users.views import register, message, user_profile
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path("message/", message, name="message"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="music/landing-page.html"), name="logout"),
    path("profile/", user_profile, name="user-profile")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)