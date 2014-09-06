from django.contrib.auth import logout
from django.shortcuts import redirect, render

from events.models import Location


def home(request):
    locations = Location.objects.all()

    return render(request, "home.html", ({
        'locations': locations
    }))