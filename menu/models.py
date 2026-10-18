from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.years_of_experience} yoe"


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook)

    def __str__(self) -> str:
        return self.name
