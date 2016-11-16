#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
#from datetime import datetime
import collections

#startTime = datetime.now()

urls = collections.defaultdict(list)

def test(URL, number):
    site = requests.get(URL).text
    soup = BeautifulSoup(site, "lxml")
    for a in soup.find_all('a', href=True):
        if re.search('^(http|https):\/\/', a['href']):
            urls[number].append(a['href'])
        else:
            urls[number].append(URL + a['href'])

def runer(URL, counts):
    test(URL, 1)
    if counts >= 2:
        c = 2
        while c <= counts:
            for x in urls[c - 1]:
                print("getting links from: ", x, "using dictionary number: ", c - 1)
                test(URL, c)
            c += 1

def checker(URL, counts):
    runer(URL, counts)
    for x in urls[counts]:
        print("For link: ", x, "status code is: ", requests.get(x).status_code)

if __name__ == "__main__":
    checker(URL='http://google.com', counts=1)

#print(datetime.now() - startTime)
