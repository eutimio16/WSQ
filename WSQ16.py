def car(file):
	c=0
	sumprice= 0
	sumcity= 0
	sumhigh= 0
	for line in file:
		c=c+1
		if(c%2==1):
			price = line[42:46]
			prices = float(price)
			sumprice= sumprice+prices
			citympg = line[52:54]
			citympg2 = float(citympg)
			sumcity= sumcity+citympg2
			high = line[55:57]
			high2 = float(high)
			sumhigh= sumhigh+high2
	cars=c/2
	average_price= sumprice/cars
	average_citympg= sumcity/cars
	average_high= sumhigh/cars
	return(average_price, average_citympg, average_high)
	
f= open("93cars.dat.txt", "r")
(a,b,c) = car(f)
a= str(a)
b= str(b)
c= str(c)
print("The average range price in $1000 is: ", a[0:5])
print("The average city MPG is: ", b[0:5])
print("The average highway MPG is: ", c[0:5])
