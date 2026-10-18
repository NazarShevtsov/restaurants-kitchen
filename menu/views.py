from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from menu.models import Cook, Dish


@login_required
def index(request) -> HttpResponse:

    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session[num_visits] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_visits": num_visits + 1,
    }
    return render(request, "menu/index.html", context=context)


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    template_name = "menu/dish-list.html"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "menu/dish-detail.html"