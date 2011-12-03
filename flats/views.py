#coding: utf-8
from datetime import datetime, date
import urllib
import xlrd
from django.template.response import TemplateResponse
from flats.models import ObjectsHistory

def show_chart(request):
    if not ObjectsHistory.objects.filter(date=date(2011, 12, 3)):
        objects = process_xls()
    else:
        objects = ObjectsHistory.objects.order_by('object_name')
    names = set(x.object_name for x in objects)
    return TemplateResponse(request, 'flats.html', {'objects' : objects, 'names' : names})

def process_xls():
    prices_local_path = './flats/prices.xls'
    urllib.urlretrieve(settings.URL_PRICE, prices_local_path)

    prices = []
    try:
        book = xlrd.open_workbook(prices_local_path)
        sh = book.sheet_by_index(0)
        for rownum in range(sh.nrows):
            prices.append(sh.row_values(rownum))
    except IOError:
        error = "Unable to open file " + prices_local_path
        print error
        return False

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

#    print datetime.today(), datetime.now()
    for building in buildings.keys():
#        print building, buildings[building]
        if not ObjectsHistory.objects.filter(
                object_name=building,
                date=datetime.today()
                ):
            print "Saving %s" % building
            ObjectsHistory.objects.create(object_name=building.encode('utf-8'), flats_count=buildings[building], date=datetime.now().date())

    return buildings
