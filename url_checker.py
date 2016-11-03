#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

startTime = datetime.now()

URL = 'http://volia.com'
list_links = []

def create_list():
    global new_list
    new_list = []
    #new_list is global list - possible to use in any place of this script

def urls(URL):
    site = requests.get(URL).text
    soup = BeautifulSoup(site, "lxml")
    links = soup.find_all('a')
#    global list_links
#    list_links = []
    for a in soup.find_all('a', href=True):
        if re.search('^(http|https):\/\/', a['href']):
            list_links.append(a['href'])
        else:
            list_links.append(URL + a['href'])

urls(URL)

for x in list_links:
    print("For link: ", x, "status code is: ", requests.get(x).status_code)

#r = requests.get('http://google.com')
#print(r.status_code)

print(datetime.now() - startTime)