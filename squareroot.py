#solution to weekly task 06
#Author: Tosin Araba

#Please enter a positive number: 14.5
#The square root of 14.5 is approx. 3.8.

n = float(input("please enter a positive number: "))
approx=0.5*n
better=0.5*(approx+n/approx) #newtons square rrot method. 
#Found https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method

while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)

print("The square root of {} is approx {}".format(n, round(better,1)))