#coding: utf-8
import xlrd
import urllib
from django.template.response import TemplateResponse
from django.conf import settings
from re import match

def show_chart(request):
    prices_local_path = './flats/prices.xls'
    urllib.urlretrieve(settings.URL_PRICE, prices_local_path)

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
            objects_list.append((row[1], rownum))


    return TemplateResponse(request, 'flats.html', {
        'error' :error,
        })


