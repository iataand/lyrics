import requests
import time
import urllib2
from bs4 import BeautifulSoup

url = "http://www.mldb.org/artist-56-red-hot-chili-peppers.html"
req = requests.get(url)

soup = BeautifulSoup(req.content, features="html.parser")

links = soup.find_all("a")
songUrls = []
bandUrls = []



for url in songUrls:
  time.sleep(5)
  checkCon(url)
  req = requests.get(url)
  soup = BeautifulSoup(req.content, features="html.parser")

  lyrs = soup.find_all("p")

  for lyr in lyrs:
    print lyr.text.encode("utf-8")
    print "________________________________________________________________________________"

def checkCon(url):  #Checking connection to the url
  try:
    urllib2.urlopen(url, timeout=1)

  except:
    return False

def findSongs():
  checkCon(url)
  links = soup.find_all("a")
  for link in links:  #Getting a list of urls with songs
    if "song" in link.get("href"):
      songUrls.append("http://www.mldb.org/" + link.get('href'))
