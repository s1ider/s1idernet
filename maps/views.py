# coding: utf-8
from urllib import urlencode,urlopen
from django.template.response import TemplateResponse
from maps.models import SearchHistory
import json

def search(request):
	if request.method == 'POST':
		search_query = request.POST['search']
		params = urlencode({
			'geocode' : search_query,
			'format' : 'json',
			'key' : 'ALkUyk4BAAAApRinSwIAS_pBYGgk9hlNbOWvjOx3Zi8VGBIAAAAAAAAAAADG1QihAV-jqGTltsWsd3ylJFXKPw=='
		})
		response_json = urlopen('http://geocode-maps.yandex.ru/1.x/', params)
		response = json.load(response_json)
		if 'error' in response:
			result = "Error has happened: " + response['error']['message']
        response = response['response']['GeoObjectCollection']['featureMember']
        if len(response) > 0:
		    result = response[0]['GeoObject']['Point']['pos']
        else:
            result = "Object '%s' was not found." % (search_query)
	return TemplateResponse(request, 'maps.html', {
		'search_text' : search_query,
		'result' : result})