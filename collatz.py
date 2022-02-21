# solution to weekly task 04

# Program that aks the user to input any positive integer
# And outputs the successive values of the following calculation
# At each step calculate the next value by taking current value
# If even divide by 2
# If odd multiply by 3 + 1
# End program if value = 1

# Author: Tosin Araba


def collatz(number):
   
    if (number % 2 == 0):
        print(number // 2)
        return number // 2

    elif (number % 2 == 1):
        result = number * 3 +1
        print(result)
        return result

number = int(input("Enter a number: "))
while number != 1:
    number = collatz(int(number))
    
