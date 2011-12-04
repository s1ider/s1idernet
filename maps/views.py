#coding: utf-8
from urllib import urlencode,urlopen
from django.conf import settings
from django.template.response import TemplateResponse
from maps.models import SearchHistory
import json

def search(request):
    search_query = request.REQUEST.get('search', '')
    result = ''
    points = []
    if search_query:
        search_query = "Киев ".decode('utf-8') + search_query
        params = urlencode({
            'geocode' : search_query.encode('utf-8'),
            'format' : 'json',
            'key' : settings.API_KEY
        })
        response_json = urlopen('http://geocode-maps.yandex.ru/1.x/', params)
        response = json.load(response_json)

        if 'error' in response:
            result = "Error has happened: " + response['error']['message']
        if 'response' in response:
            response = response['response']['GeoObjectCollection']['featureMember']
        if len(response) > 0:
            for obj in response:
                x,y = (obj['GeoObject']['Point']['pos'].split(' '))
                points.append([float(x), float(y)])
        else:
            result = "Извините, не смогли найти '%s'." % search_query
    return TemplateResponse(request, 'maps.html', {
        'API_KEY' : settings.API_KEY,
        'search_text' : search_query[5:],   # remove Киев from search_text
        'result' : result,
        'points' : json.dumps(points),
        })