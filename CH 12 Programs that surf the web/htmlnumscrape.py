# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#url = 'http://python-data.dr-chuck.net/comments_42.html'
url = 'http://python-data.dr-chuck.net/comments_367314.html'
html = urlopen(url).read()
soup = BeautifulSoup(html,"lxml")

# Retrieve all of the anchor tags
numlist=list()
count=0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print ('TAG:',tag)
    num=re.findall('>([0-9]+)<',str(tag))
    for n in num:
     numhold=float(n)
     numlist.append(numhold)
    count=count+1

print('count is',count,'and sum is',sum(numlist))