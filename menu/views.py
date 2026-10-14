from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required
def index(request) -> HttpResponse:
    context = {}
    return render(request, "menu/index.html", context=context)