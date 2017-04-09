hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
h = float(hrs)
r=float(rate)

if h < 40.0:
	pay=h*r
elif h>40.0:
	timehalf=float(h-40)
	pay=40*r+(1.5*timehalf*r)   
print pay