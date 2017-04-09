# Use the file name mbox-short.txt as the file name
total=0
count=0
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    ind=line.find(": ")
    total=total+float(line[ind+1:])
    count=count+1
    
avg=total/count    
print "Average spam confidence:",avg