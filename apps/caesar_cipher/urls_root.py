from django.urls import path
from apps.caesar_cipher import views

app_name = "root"

urlpatterns = [
    path("", views.index, name="index"),
]
