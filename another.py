#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import collections

startTime = datetime.now()

website = 'http://volia.com'
urls = collections.defaultdict(list)

def test(URL, number):
    site = requests.get(URL).text
    soup = BeautifulSoup(site, "lxml")
    for a in soup.find_all('a', href=True):
        if re.search('^(http|https):\/\/', a['href']):
            urls[number].append(a['href'])
#            print(a['href'])
        else:
            urls[number].append(URL + a['href'])
#            print(URL + a['href'])
#test(website, number=1)

def runer(counts):
    test(website, 1)
    if counts >= 2:
        c = 2
        while c <= counts:
            for x in urls[c - 1]:
                print("getting links from: ", x, "using dictionary number: ", c - 1)
                test(website, c)
            c += 1
runer(counts=2)

#print("FIRST URLS")
#print('URLS from 1: ', urls[1])
#print("Second URLS")
#print('URLS from 2: ', urls[2])
#print("Third URLS")
#print('URLS from 3: ', urls[3])

for xx in urls[1]:
    print("For link: ", xx, "from dictionary 1, status code is: ", requests.get(xx).status_code)
for xy in urls[2]:
    print("For link: ", xy, "from dictionary 2, status code is: ", requests.get(xy).status_code)
for xz in urls[3]:
    print("For link: ", xz, "from dictionary 3, status code is: ", requests.get(xz).status_code)


print(datetime.now() - startTime)