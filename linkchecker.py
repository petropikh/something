#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
import collections

class LinkChecker:
    def __init__(self, URL):
        self.URL = URL
        if requests.get(URL).status_code != 200:
            raise SystemError('Wrong URL: ' + URL + ' status code is: ' + str(requests.get(URL).status_code))

    urls = collections.defaultdict(list)
    uniqurls = []

    def getter(self):
        site = requests.get(self.URL).text
        soup = BeautifulSoup(site, "lxml")
        for a in soup.find_all('a', href=True):
            if re.search('^(http|https):\/\/', a['href']):
                self.urls[self.URL].append(a['href'])
#DEBUG                print(a['href'])
            else:
                self.urls[self.URL].append(self.URL + a['href'])
#DEBUG                print(self.URL + a['href'])

    def find_duplicates(self):
        self.getter()
#        uniqurl = []
        for x in range(len(self.urls[self.URL])):
            if self.uniqurls.count(self.urls[self.URL][x]) == 0:
                self.uniqurls.append(self.urls[self.URL][x])
#DEBUG        print(self.uniqurl)

    def status(self):
        self.find_duplicates()
        for x in self.uniqurls:
            try:
                print('For URL: ' + x + 'status code is: ' + str(requests.get(x, timeout=0.5).status_code))
            except OSError:
                print('Something wrong happens for URL: ' + x)


x = LinkChecker(URL='http://google.com')
#x.getter()
#x.find_duplicates()
x.status()
