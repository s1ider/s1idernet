# coding: utf-8
from urllib import urlencode,urlopen
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from flats.models import SearchHistory
import simplejson

def search(request):
	if request.method == 'POST':
		search_query = request.POST['search']
		params = urlencode({
			'geocode' : search_query,
			'format' : 'json',
			'api' : u'ALkUyk4BAAAApRinSwIAS_pBYGgk9hlNbOWvjOx3Zi8VGBIAAAAAAAAAAADG1QihAV-jqGTltsWsd3ylJFXKPw=='
		})
		response_json = urlopen('http://geocode-maps.yandex.ru/1.x/', params)
		result = simplejson.load(response_json)
		if 'error' in result:
			result = "Error has happened: " + result['error']['message']
	else:
		pass
	return TemplateResponse(request, 'flats.html', {
		'search_text' : search_query,
		'result' : result})