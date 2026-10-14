from django.urls import path, include

from menu.views import index

urlpatterns = [
    path("", index, name="index"),
    path("accounts/", include("django.contrib.auth.urls"))
]

app_name = "menu"