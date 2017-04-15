from urllib.request import urlopen
import urllib.parse
import xml.etree.ElementTree as ET


#url = 'http://python-data.dr-chuck.net/comments_42.xml' #test url where summation should be 2553
url = 'http://python-data.dr-chuck.net/comments_367311.xml' #real data

print ("retrieving",url)
uh = urllib.request.urlopen(url)
data=uh.read()
print ('Retrieved',len(data),'characters')

tree = ET.fromstring(data)
counts = tree.findall('.//count')
summation=0
for count in counts:
 summation=summation+int(count.text)
print("Sum:",summation)