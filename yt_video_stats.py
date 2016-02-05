"""
Takes a Youtube video link and returns some stats.
"""

from bs4 import BeautifulSoup
import re
import requests

url = input('Link to Youtube video: ')

r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')

views = soup.find('div', {'class':'watch-view-count'})
views = views.get_text()

uploaded_date = soup.find('strong', {'class':'watch-time-text'})
uploaded_date = uploaded_date.get_text()

spans = soup.find_all('span', {'class':'yt-uix-button-content'})
lines = [span.get_text() for span in spans]

pattern = re.compile(r'^[\d\s,]*$')
matches = []

for line in lines:
    if pattern.match(line):
        matches.append(line)

print('Views:', views)
print('Upvotes:', matches[0])
print('Downvotes:', matches[2])
print(uploaded_date)
