from django.urls import path

from .views import IndexView, LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", IndexView.as_view(), name="index"),
]
