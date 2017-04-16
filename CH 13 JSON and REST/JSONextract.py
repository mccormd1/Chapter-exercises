import json
from urllib.request import urlopen
#url='http://python-data.dr-chuck.net/comments_42.json' #test that sums to 2553
url='http://python-data.dr-chuck.net/comments_367315.json'
input=urlopen(url)
data=input.read()
print(len(data),'Characters')
info = json.loads(data)
#print (json.dumps(info,indent=4))
print('Count:',len(info['comments']))

sum=0
for item in info['comments']:
    #print ('name:', item['name'])
    #print ('count', item['count'])
    sum=sum+int(item['count'])
print(sum)