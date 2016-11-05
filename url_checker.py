#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

startTime = datetime.now()

website = 'http://google.com'
list_links = []

class checker():
    def urls(URL):
        site = requests.get(URL).text
        soup = BeautifulSoup(site, "lxml")
        links = soup.find_all('a')
        for a in soup.find_all('a', href=True):
            if re.search('^(http|https):\/\/', a['href']):
                list_links.append(a['href'])
            else:
                list_links.append(URL + a['href'])
#        for x in list_links:
#            print("For link: ", x, "status code is: ", requests.get(x).status_code)

checker.urls(website)

for x in list_links:
    checker.urls(x)



print(datetime.now() - startTime)