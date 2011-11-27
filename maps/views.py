# coding: utf-8
from urllib import urlencode,urlopen
from django.conf import settings
from django.template.response import TemplateResponse
from maps.models import SearchHistory
import json

def search(request):
    search_query = request.REQUEST.get('search', '')
    result = ''
    if search_query:
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
            result = response[0]['GeoObject']['Point']['pos']
        else:
            result = "Object '%s' was not found." % search_query
    return TemplateResponse(request, 'maps.html', {
        'API_KEY' : settings.API_KEY,
        'search_text' : search_query,
        'result' : result})