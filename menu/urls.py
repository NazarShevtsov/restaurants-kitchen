from django.urls import path
from django.views import View

from menu.views import index, DishListView, DishDetailView, DishTypeListView, CookListView, CookDetailView, \
    CookCreateView, CookUpdateView, CookDeleteView, DishTypeDeleteView, DishTypeCreateView, DishCreateView, \
    DishUpdateView, DishDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-type/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("dish-type/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
]

app_name = "menu"