import re

#name='regex_sum_42.txt'
name='regex_sum_367309.txt'
fh=open(name)
allnumlist=list()
for line in fh:
 line=line.strip()
 listnum=re.findall('([0-9]+)',line)
 listlength=len(listnum)
 if listlength == 0: continue
 for n in listnum:
  num=float(n)
  allnumlist.append(num)
count=0
sumall=0
for i in allnumlist:
 sumall=sumall+i
 count=count+1
print ('count is',count,'and sum is',sumall)