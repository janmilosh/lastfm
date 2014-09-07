from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import datetime

from events.models import Location

def save_location(request):
    city = request.POST.get('city', '')
    state = request.POST.get('state', '')

    location = Location(city=city, state=state, timestamp=timezone.now(), user=request.user)
    location.save()

    name = '%s, %s' % (city, state)

    return render(request, 'events/show_events.html', ({
        'location': name,
    }))

def get_events(request, location_id=1):
    location = get_object_or_404(Location, id=location_id)
    location.name = '%s, %s' % (location.city, location.state)

    return render(request, 'events/show_events.html', ({
        'location': location.name
    }))
