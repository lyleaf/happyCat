import requests 
from bs4 import BeautifulSoup
import ctypes
import struct
from PIL import Image


dep="NCE"
dest="FCO"
dd="2017-01-18"
rd="2017-01-20"

url = "http://www.easyjet.com/links.mvc?lang=FR&dep=%s&dest=%s&dd=%s&rd=%s&apax=1&cpax=0&ipax=0&SearchFrom=SearchPod2&isOneWay=off&pid=" % (dep,dest,dd,rd)
print url
r = requests.get(url)

soup = BeautifulSoup(r.text)
soup.findAll("ul",{"class" : "middleRow"})[0].findAll("a")[0]['charge-credit-full']
soup.findAll("ul",{"class" : "middleRow"})[-1].findAll("a")[0]['charge-credit-full']
