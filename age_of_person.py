"""
Takes the full name of a person as input and returns the
person's current age and date of birth.
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

age = soup.find('span', {'class':'bday'})
age = ''.join(map(str, age.contents)).strip()
age = datetime.datetime.strptime(age, '%Y-%m-%d')
agef = age.strftime('%B %d, %Y')

now = datetime.datetime.now()
nowf = now.strftime('%Y-%m-%d')

diff = relativedelta(now, age).years

print(str(diff) + ' years')
print(agef)
