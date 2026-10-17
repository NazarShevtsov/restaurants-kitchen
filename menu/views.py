from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

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