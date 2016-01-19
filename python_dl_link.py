"""
Returns the download link to the Windows x86-64 executable
installer for the latest stable release of Python.
"""

import re

from bs4 import BeautifulSoup
import requests

url = 'https://www.python.org/ftp/python/'

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

links = soup.findAll('a')

pattern = re.compile(r'^\d[.]\d([.]\d)?/$')

versions = []

for a in links:
    if pattern.match(a['href']):
        versions.append(a['href'].replace('/', ''))

version = versions[-1]

print('{0}{1}/python-{1}-amd64.exe'.format(url, version))
