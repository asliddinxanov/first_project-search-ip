#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 09:17:48 2022

@author: asliddinxanov
"""

import requests
from pyfiglet import Figlet
# import folium

def info_ip(query = '24.48.0.1'):
    try:
        response = requests.get(url = f'http://ip-api.com/json/{query}').json()
        data = {
            'IP' : response.get('query'),
            'INT Povider' : response.get('isp'),
            'Org' : response.get('org'),
            'Country' : response.get('counrty'),
            'Region Name' : response.get('regionName'),
            'City' : response.get('city'),
            'ZIP' : response.get('zip'),
            'Lat' : response.get('lat'),
            'Lon' : response.get('lon')}
        for a,b in data.items():
            print(f'{a} : {b}')
            
        # area = folium.Map(location=[response.get('lat'), response.get('lon')])
        # area.save(f'{response.get("query")}_{response.get("city")}.html')
            
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!!!')
        
def main():
    preview_text = Figlet(font = 'slant')
    print(preview_text.renderText('SEARCH IP ADDRESS'))
    ip = input('Please ENTER IP address: ')

    info_ip(query = ip)

if __name__ == '__main__':
    main()        