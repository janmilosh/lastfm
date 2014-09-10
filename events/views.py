from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime
from dateutil import parser
import requests

from events.models import Location

@login_required(login_url='/login/')
def set_location(request):
    city = request.POST.get('city', '')
    state = request.POST.get('state', '')
    lat = str(request.POST.get('lat', ''))
    lon = str(request.POST.get('lon', ''))

    name = '%s, %s' % (city, state)
    
    if not lat:
        location_array = get_lat_lon(name)
        lat = location_array[0]
        lon = location_array[1]

    location = Location(city=city, state=state, lat=lat, lon=lon, timestamp=timezone.now(), user=request.user)
    location.save()

    location.name = name;

    events = get_events_from_lastfm(lat, lon)

    return render(request, 'events/show_events.html', ({
        'location': location,
        'events': events,
    }))

@login_required(login_url='/login/')
def get_events(request, location_id=1):
    location = get_object_or_404(Location, id=location_id)
    
    location.name = '%s, %s' % (location.city, location.state)

    events = get_events_from_lastfm(location.lat, location.lon)

    return render(request, 'events/show_events.html', ({
        'location': location,
        'events': events,
    }))

@login_required(login_url='/login/')
def delete(request, location_id=1):
    location = get_object_or_404(Location, id=location_id)
    
    location.delete()
    
    return redirect('/')

def get_lat_lon(name): #from google geocode api, get lat and lon from city, state
    key = 'AIzaSyDe1fq7oib8shkDokkXzJ8H1txRTLjR8k8'
    
    geolocation = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + name + '&sensor=false&key=' + key)
    geolocation = geolocation.json();
    
    lat = geolocation['results'][0]['geometry']['location']['lat']
    lon = geolocation['results'][0]['geometry']['location']['lng']
    
    location = [str(lat), str(lon)]
    
    return location

def get_events_from_lastfm(lat, lon): #user latitude and longitude to get the lastfm events
    key =  '0e46d3e54e84eac74e6c29e3212915ac'

    try:
        events = requests.get('http://ws.audioscrobbler.com/2.0/?method=geo.getevents&lat='+ lat + '&long=' + lon + '&api_key=' + key + '&format=json')
        eventsdata = events.json()['events']['event']

        # we need to flatten this data and make it more accessible (create an array of objects)
        event_list = []
        for event in eventsdata:

            # Convert the time into a datetime object
            event_date = event['startDate']
            event_date = parser.parse(event_date)
            artist = event['artists']['headliner']
            artist_ugly = artist.replace('&', 'ampersand_symbol')
            artist_slug = slugify(artist_ugly)

            event_list.append({
                'artist': artist,
                'artist_slug': artist_slug,
                'venue': event['venue']['name'],
                'lat': event['venue']['location']['geo:point']['geo:lat'],
                'lon': event['venue']['location']['geo:point']['geo:long'],
                'street': event['venue']['location']['street'],
                'city': event['venue']['location']['city'],
                'url': event['venue']['url'],
                'image': event['venue']['image'][3]['#text'],
                'date': event_date,
            })

    except:
        event_list = {'message': 'There are no events, please try another location.'}

    return event_list

def get_artist(request, artist, location_id):
    key =  '0e46d3e54e84eac74e6c29e3212915ac'
    artist = artist.replace('ampersand_symbol', '%26')
    artist_unslugged = artist.replace('-', '%20')
    
    try:
        artistdata = requests.get('http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&autocorrect=1&artist='+ artist_unslugged + '&api_key=' + key + '&format=json')

        artistdata = artistdata.json()['artist']
        artist = {
            'name': artistdata['name'],
            'image': artistdata['image'][4]['#text'],
            'bio': artistdata['bio']['content'],
        }
        location = {
            'id': location_id,
        }
        
    except:
        artist = {'message': "Sorry, we couldn't find any info on that artist."}

    return render(request, 'events/show_artist.html', ({
        'artist': artist,
        'location': location
    }))
