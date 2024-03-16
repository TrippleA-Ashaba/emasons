from django.urls import path

from .views import CalculatorView, IndexView

app_name = "inventory"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("calculator/", CalculatorView.as_view(), name="calculator"),
]
