#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import collections

startTime = datetime.now()

website = 'http://google.com'
deep = 2


list_links = []

class checker():
    def urls(URL, DEEP):
        site = requests.get(URL).text
        soup = BeautifulSoup(site, "lxml")
        links = soup.find_all('a')
        for a in soup.find_all('a', href=True):
            if re.search('^(http|https):\/\/', a['href']):
                list_links.append(a['href'])
            else:
                list_links.append(URL + a['href'])
        for x in list_links:
            print("For link: ", x, "status code is: ", requests.get(x).status_code)

#checker.urls(website, deep)


count = 3
urls = {}
urls = collections.defaultdict(list)

def test(count):
    с = 1
    while с <= count:
        site = requests.get('http://google.com').text
        soup = BeautifulSoup(site, "lxml")
        links = soup.find_all('a')
        for a in soup.find_all('a', href=True):
            if re.search('^(http|https):\/\/', a['href']):
                urls[с].append(a['href'])
            else:
                urls[с].append('http://google.com' + a['href'])
        с += 1

test(count)
print(urls[1])




#link = 'link' + str(1)
#print(link)

print(datetime.now() - startTime)