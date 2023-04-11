from django.urls import path

from apps.caesar_cipher import views

app_name = "caesar_cipher"

urlpatterns = [
    path("crypto/", views.MessageView.as_view(), name="crypto"),
]
