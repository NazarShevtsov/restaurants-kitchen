from django.urls import path, include

from menu.views import index, DishListView, DishDetailView, DishTypeListView, CookListView, CookDetailView, \
    CookCreateView, CookUpdateView

urlpatterns = [
    path("", index, name="index"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
]

app_name = "menu"