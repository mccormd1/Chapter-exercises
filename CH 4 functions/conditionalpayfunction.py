def computepay(h,r):

    if h <=40:
        pay=h*r
    elif h >40:
        timehalf=(h-40)
        pay=40*r+(1.5*timehalf*r)
    return pay

hrs = raw_input("Enter Hours:")
rate= raw_input("Enter Rate:")
hrs=float(hrs)
rate=float(rate)
p = computepay(hrs,rate)
print p