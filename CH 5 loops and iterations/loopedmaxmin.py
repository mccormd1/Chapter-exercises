largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    try:
        n=int(num)
    except:
        print "Invalid input"
    if num == "done":
        break
    if largest is None:
        largest=n
    elif n>largest:
        largest=n
    if smallest is None:
        smallest=n
    elif n<smallest:
    	smallest=n
print "Maximum is", largest
print "Minimum is", smallest