#coding: utf-8
from datetime import datetime, date
import urllib
import xlrd
import json
from django.template.response import TemplateResponse
from django.conf import settings
from flats.models import FlatsNumber, Buildings

def show_chart(request):
    if not FlatsNumber.objects.filter(date=datetime.today().date()):
        buildings = process_xls()
    else:
        buildings = {}
        buildings_list = Buildings.objects.all()
        for building in buildings_list:
            flats = FlatsNumber.objects.get(building=building)
            buildings[building.name] = (flats.one_room, flats.two_rooms, flats.three_rooms, flats.four_or_more_rooms)

    names = []
    for id, name in Buildings.objects.values_list():
        names.append(name)

    return TemplateResponse(request, 'flats.html', {'names': names, 'buildings': json.dumps(buildings)})

def process_xls():
    prices_local_path = settings.BASE_DIR + '/flats/prices.xls'
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
    (one_room_counter, two_rooms_counter, three_rooms_counter, four_or_more_rooms_counter) = (0, 0, 0, 0)
    for row in prices:
        if row[1]:
            buildings[name] = (one_room_counter, two_rooms_counter, three_rooms_counter, four_or_more_rooms_counter)
            name = row[1]
            (one_room_counter, two_rooms_counter, three_rooms_counter, four_or_more_rooms_counter) = (0, 0, 0, 0)
        if row[6] == 1:
            one_room_counter += 1
        elif row[6] == 2:
            two_rooms_counter += 1
        elif row[6] == 3:
            three_rooms_counter += 1
        elif row[6] >= 4 and row[2] != u'Разом:':
            four_or_more_rooms_counter += 1
    del buildings['']

    for building in buildings.keys():
        today_date = datetime.today().date()
        if not FlatsNumber.objects.filter(building=Buildings.objects.filter(name=building),
                                          date=today_date):
            building_model = Buildings.objects.filter(name=building)
            if not building_model:
                building_model = Buildings.objects.create(name=building)
            FlatsNumber.objects.create(building=building_model, one_room=buildings[building][0], two_rooms=buildings[building][1],
                                       three_rooms=buildings[building][2], four_or_more_rooms=buildings[building][3],
                                       date=today_date)
    return buildings
