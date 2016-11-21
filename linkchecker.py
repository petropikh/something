#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
import collections
from datetime import datetime

startTime = datetime.now()

class LinkChecker:
    def __init__(self, URL, count):
        self.URL = URL
        if requests.get(URL, timeout=5).status_code != 200:
            raise SystemError('Wrong URL: ' + URL + ' status code is: ' + str(requests.get(URL).status_code))
        self.urls = collections.defaultdict(list) # Here, you just initialing a list after a first check of the base url
        self.uniq = collections.defaultdict(list)
        self.url_to_status_dic = dict()
        self.count = count

    c = 0

    def collect_urls(self):
        site = requests.get(self.URL).text
        soup = BeautifulSoup(site, "lxml")
        for a in soup.find_all('a', href=True):
            if re.search('^(http|https):\/\/', a['href']):
                self.urls[self.c].append(a['href'])
            else:
                self.urls[self.c].append(self.URL + a['href'])

    def find_duplicates(self):
        seen = set() # this is a collection structure that does not permit duplications
        self.uniq[self.c] = [x for x in self.urls[self.c] if x not in seen and not seen.add(x)]

    def find_link_status(self):
        for link in self.uniq[self.c]:
            try:
                self.url_to_status_dic.update({link: requests.get(link, timeout=0.5).status_code})
            except OSError:
                print("Something wrong happens for URL: {}".format(link))

    def run(self):
        while self.c < self.count:
            self.collect_urls()
            self.find_duplicates()
            self.find_link_status()
            for x in self.uniq[self.c - 1]:
                self.collect_urls()
                self.find_duplicates()
                self.find_link_status()
            self.c += 1


if __name__ == '__main__':
    lc = LinkChecker('http://www.google.com', 1)
    lc.run()
    for k, v in lc.url_to_status_dic.items():
        print("{} -> {}".format(k, v))
    print(datetime.now() - startTime)
