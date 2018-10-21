import requests
import time
import urllib2
from bs4 import BeautifulSoup

artistList = []
songList = []
lyrsList = []

def checkCon(url):
  try:
    urllib2.urlopen(url, timeout=1)
    return True
  except: 
    return False

def getArtists(url):
  if(checkCon(url)):
    time.sleep(3)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, features="html.parser")

    artists1 = soup.find_all('tr', 'h')
    artists2 = soup.find_all('tr', 'n')

    for artist1, artist2 in zip(artists1, artists2):
      url = "http://www.mldb.org/" + str(artist1.contents[1].find('a').get('href'))
      artistList.append(url)

      url = "http://www.mldb.org/" + str(artist2.contents[1].find('a').get('href'))
      artistList.append(url)

def getSongs(url):
  time.sleep(3)
  req = requests.get(url)
  soup =BeautifulSoup(req.content, features="html.parser")

  links = soup.find_all('a')
  for link in links: 
    if "song" in link.get('href'):
      songList.append("http://mldb.org/" + str(link.get('href')))

x = 0

while x <= 870:
  url = "http://www.mldb.org/aza-A-" + str(x) + ".html"
  getArtists(url)

  for url in artistList:
    getSongs(url)

    for song in songList:
      time.sleep(3)
      req = requests.get(song)
      soup = BeautifulSoup(req.content, features="html.parser")

      lyrs = soup.find_all('p')
      for lyr in lyrs:
        print lyr.text.encode('utf-8')
        #lyrsList.append(lyr.text.encode('utf-8'))
        
  x += 30
