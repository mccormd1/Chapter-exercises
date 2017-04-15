# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html' #test one, ends with Anayah
url = 'http://python-data.dr-chuck.net/known_by_Davis.html' 
numlinks=int(input("Input number of links: "))
position=int(input("Input start position: "))
# Retrieve all of the anchor tags
numlist=list()
count=0
print(url)
for i in range(numlinks):
 html = urlopen(url).read()
 soup = BeautifulSoup(html,"lxml")
 tags = soup('a')
 tag=tags[position-1]
 print(tag.get('href', None))
 url=tag.get('href', None)
