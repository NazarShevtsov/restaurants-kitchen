from django.contrib import admin

from menu.models import Dish, DishType, Cook


# Register your models here.
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price")
    list_filter = ["dish_type"]


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "years_of_experience",)
    list_filter = ("years_of_experience",)
    search_fields = ("username", "first_name", "last_name",)
