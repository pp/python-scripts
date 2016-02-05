"""
Takes the full name of a person as input and returns the person's date
of birth and current age. If the person is deceased, the date of birth
and death and the age at death is returned.
"""

import datetime

from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import requests

name = input('Name: ')
name.replace(' ', '_')

url = 'https://en.wikipedia.org/wiki/' + name

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

bday = soup.find('span', {'class':'bday'})
if bday is not None:
    bday = bday.get_text()
    bday = datetime.datetime.strptime(bday, '%Y-%m-%d')

dday = soup.find('span', {'class':'dday'})
if dday is not None:
    dday = dday.get_text()
    dday = datetime.datetime.strptime(dday, '%Y-%m-%d')

if bday is not None:
    born = 'Born: ' + bday.strftime('%B %d, %Y')
    if dday is None:
        now = datetime.datetime.now()
        diff = relativedelta(now, bday).years
        born += ' (age {0})'.format(diff)
        print(born)
    else:
        diff = relativedelta(dday, bday).years
        died = ('Died: ' + dday.strftime('%B %d, %Y') +
               ' (aged {0})'.format(diff))
        print(born)
        print(died)
else:
    print('There is no person with this name.')
