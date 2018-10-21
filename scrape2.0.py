import requests
import time
import urllib2
from bs4 import BeautifulSoup

def checkCon(url):
  try:
    urllib2.urlopen(url, timeout=1)
    return True
  except: 
    return False

x = 0

url = "http://www.mldb.org/aza-A-" + str(x) + ".html"
if(checkCon(url)):
  req = requests.get(url)
  soup = BeautifulSoup(req.content, features="html.parser")

  artists1 = soup.find_all('tr', 'h')
  artists2 = soup.find_all('tr', 'n')

  id = 0
  artistsUrl = []

  for artist1 in artists1:
    url = "http://www.mldb.org/" + str(artist1.contents[1].find('a').get('href'))
    artistsUrl.insert(id, url)
    id += 2
  
  id = 1

  for artist2 in artists2:
    url = "http://www.mldb.org/" + str(artist2.contents[1].find('a').get('href'))
    artistsUrl.insert(id, url)
    id += 2

  for url in artistsUrl:
    print url