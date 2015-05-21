#!/usr/bin/env python

import sys
import requests
import os

def get_weather(query, key):
    try:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s&units=imperial' % (query, key))
    except Exception as e:
        print e
    


    if r.status_code == 200:
        result = r.json()
        print result['name']
        print result['main']['temp']
    else:
        print 'api fucked up %s' % r.status_code
        for header, value in r.headers.iteritems():
            print '%s: %s' % (header, value)
        print r.text
    

def main():
    key = os.environ.get('weather_key')
    print key

    if len(sys.argv) > 1:
       location = sys.argv[1]
       get_weather(location, key)
    else:
        print 'You need to provide an argument'


if __name__ == "__main__":
    main()

