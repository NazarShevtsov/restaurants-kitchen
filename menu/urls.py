from django.urls import path, include

from menu.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "menu"