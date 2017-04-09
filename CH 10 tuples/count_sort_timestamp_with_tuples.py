name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hourcount=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        timestamp=words[5]
        time=timestamp.split(':')
        time=time[0:1]
        for hour in time:
            hourcount[hour]=hourcount.get(hour,0)+1
            
sorthour=sorted([(k,v) for k,v in hourcount.items()])            

for key,val in sorthour:
    print (key, val)