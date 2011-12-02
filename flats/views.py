#coding: utf-8
from datetime import datetime
import xlrd
import urllib
import json
from re import match
from django.template.response import TemplateResponse
from django.conf import settings
from flats.models import ObjectsHistory

def show_chart(request):
    return TemplateResponse(request, 'flats.html', {'objects' : json.dumps(process_xls())})

def process_xls():
    prices_local_path = './flats/prices.xls'
#    urllib.urlretrieve(settings.URL_PRICE, prices_local_path)

    error = ''
    prices = []
    try:
        book = xlrd.open_workbook(prices_local_path)
        sh = book.sheet_by_index(0)
        for rownum in range(sh.nrows):
            prices.append(sh.row_values(rownum))
    except IOError:
        error = "Unable to open file " + filename

    buildings = {}
    name = ''
    flats_counter = 0
    for row in prices:
        if row[1]:
            buildings[name] = flats_counter
            name = row[1]
            flats_counter = 0
        else:
            flats_counter += 1
    del buildings['']

    for building in buildings.keys():
        print building, buildings[building]
        b = ObjectsHistory(object_name=building, flats_count=buildings[building], date=datetime.now())
        b.save()

    return buildings

