from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


class LoginView(LoginView):
    template_name = "users/login.html"


class LogoutView(LogoutView):
    pass


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    extra_context = {"title": "Home"}
