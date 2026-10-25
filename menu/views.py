from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from menu.forms import CookCreationForm
from menu.models import Cook, Dish, DishType


@login_required
def index(request) -> HttpResponse:

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dishtypes = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session[num_visits] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dishtypes": num_dishtypes,
        "num_visits": num_visits + 1,
    }
    return render(request, "menu/index.html", context=context)


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("menu:dish-type-list")


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("menu:dish-type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("menu:cook-list")
    template_name = "menu/cook_create.html"


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "years_of_experience")
    success_url = reverse_lazy("menu:cook-list")
    template_name = "menu/cook_update.html"


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("menu:cook-list")