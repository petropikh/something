#!/usr/bin/python3

import urllib.request

site = urllib.request.urlopen("http://google.com").read()
print(site)

print('\nhello people')