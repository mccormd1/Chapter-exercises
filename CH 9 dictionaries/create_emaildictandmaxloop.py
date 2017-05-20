name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    if line.startswith('From '):
        words=line.split()
        names=words[1]
        count[names]=count.get(names,0)+1
 
bigcount=None
for handle, val in count.items():
    if bigcount is None or val > bigcount:
        bigcount=val
        mosthandle=handle


print (mosthandle, bigcount)

print(count)