# from django.urls import path
# from . import views
# from django.contrib.auth.decorators import login_required
#
from django.urls import path

from apps.caesar_cipher import views

app_name = "caesar_cipher"

urlpatterns = [
    path("crypto/", views.CryptoCreateView.as_view(), name="crypto"),
]
