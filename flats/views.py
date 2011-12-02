#coding: utf-8
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
            prices.append((sh.row_values(rownum), rownum))
    except IOError:
        error = "Unable to open file " + filename

    objects_list = []
    for row, rownum in prices:
        if match(r'\d',row[0]):
            current_object = row[1]
        if row[2] == u'Разом:':
            objects_list.append((current_object, int(row[5])))

#    for object_name, flats_count in objects_list:
#        print type(object_name), flats_count

    return objects_list

