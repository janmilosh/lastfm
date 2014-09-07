from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime

from events.models import Location

def save_location(request):
    name = request.POST.get('name', '')

    location = Location(name=name, timestamp=timezone.now())
    location.save()

    return render(request, 'events/show_events.html', ({
        'location': name,
    }))

def get_events(request, event_location='Columbus, Ohio'):
    location = event_location

    return render(request, 'events/show_events.html', ({
        'location': location
    }))
