from django.shortcuts import render
from .models import Ceos

# Create your views here.


def index(request):
    ceos = Ceos.objects.all()
    context = {"purplestuff": ceos}

    return render(request, "index.html", context)
