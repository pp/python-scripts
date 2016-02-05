"""
Returns the download link to the Windows x86-64 executable
installer for the latest stable release of Python.
"""

import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/ftp/python/'

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

pattern = re.compile(r'^\d[.]\d([.]\d)?/$')
versions = []

for a in soup.find_all('a', href=True):
    if pattern.match(a['href']):
        versions.append(a['href'].replace('/', ''))

print('{0}{1}/python-{1}-amd64.exe'.format(url, versions[-1]))
