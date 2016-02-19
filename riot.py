import urllib2
import sys
import json
import urlparse

base_url = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion'
url_params = '?champData=lore&api_key=e0d1c28b-804f-428b-ad20-73879024c4ad'

url = urlparse.urljoin(base_url, url_params)
response = urllib2.urlopen(url)
data = json.load(response)

def checkIfInList(champion_name):
  for result in data["data"]:
    if result == champion_name:
      return True
  return False


def get_lore(champion_name):
  lore = ''
  if checkIfInList(champion_name):
    lore = data["data"][champion_name]["title"]
    print lore
  return lore

if __name__ == "__main__": 
  get_lore("Ezreal")
