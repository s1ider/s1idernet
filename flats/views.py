from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from flats.models import SearchHistory

def search(request):
	if request.method == 'POST':
		search_query = request.POST['search']
	else:
		pass
	return TemplateResponse(request, 'flats.html', {
		'search_text' : search_query})