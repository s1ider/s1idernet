from urllib import urlencode,urlopen
from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from flats.models import SearchHistory

def search(request):
	if request.method == 'POST':
		search_query = request.POST['search']
		params = urlencode({
			'geocode' : search_query,
			'format' : 'json',
			'api' : 'ALkUyk4BAAAApRinSwIAS_pBYGgk9hlNbOWvjOx3Zi8VGBIAAAAAAAAAAADG1QihAV-jqGTltsWsd3ylJFXKPw=='
		})
		f = urlopen('http://geocode-maps.yandex.ru/1.x/', params)
		print f.read()
	else:
		pass
	return TemplateResponse(request, 'flats.html', {
		'search_text' : search_query})