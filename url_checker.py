#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re

URL = 'http://volia.com'

site = requests.get(URL).text

soup = BeautifulSoup(site, "lxml")
links = soup.find_all('a')

for a in soup.find_all('a', href=True):
#    print(a['href'])

    if re.search('^(http|https):\/\/', a['href']):
        print(a['href'])
    else:
        print(URL + a['href'])
