import requests
from copy import copy
from bs4 import BeautifulSoup
import json
import time

changed = ['station_no', 'name_tw', 'parking_spaces','available_spaces', 'empty_spaces','forbidden_spaces', 'status', 'type', 'updated_at','time']
attr = ['station_no','name_tw','district_tw','address_tw', 'name_en','district_en','address_en', 'lat','lng']

with open('~/Youbike2.0/station_data/' + time.strftime("%Y-%m-%d-%H:%M:%S-%a", time.localtime()) + '.csv', 'w') as output_file:
#with open('station_data.csv', 'w') as output_file:
    url = 'https://apis.youbike.com.tw/api/front/station/all?lang=tw&type=2'
    html = requests.get(url)
    data = json.loads(html.text)
    if data['retCode'] != 1:
        output_file.write('Getting data error: retCode = 1, {}'.format(data['retMsg']))
        exit()
    station_data = data['retVal']
    for i, clm_name in enumerate(changed):
        output_file.write(clm_name)
        output_file.write(',' if i != len(changed) - 1 else '\n')

    for station in station_data:
        for i, clm_name in enumerate(changed):
            #print('{:17s}-> {:>}'.format(item, station[item]))
            output_file.write(''.join(str(station[clm_name]).split(',')))
            output_file.write(',' if i != len(changed) - 1 else '\n')

#html.encoding = "big5"
#soup = BeautifulSoup(html.text, 'html.parser')
#soup.prettify()
#titles = soup.select('tbody[id=setarealist]')
