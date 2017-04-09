fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
wordlist=[]
for line in fh:
    nextline=line.split()
    for word in nextline:
        if word not in wordlist:
            wordlist.append(word)
            

wordlist.sort()
print wordlist
