from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
import datetime
import requests

from events.models import Location

def set_location(request):
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

    #lastfm API
    key =  '0e46d3e54e84eac74e6c29e3212915ac'
    secret = '99b690b8f5550c141e87db0d01b7a332'

    events = requests.get('http://ws.audioscrobbler.com/2.0/?method=geo.getevents&location='+ location.city + '&api_key=' + key + '&format=json')

    eventsdata = events.json()

    return render(request, 'events/show_events.html', ({
        'location': location.name,
        'eventsdata': eventsdata,
    }))

def delete(request, location_id=1):
    location = get_object_or_404(Location, id=location_id)

    location.delete()

    return redirect('/')

