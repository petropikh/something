#!/usr/bin/python3

import urllib.request

from bs4 import BeautifulSoup

site = urllib.request.urlopen("http://google.com").read()

soup = BeautifulSoup(site, "lxml")
links = soup.find_all('a')

for x in links:
    print(x)
