# solution to weekly task 04

# Program that aks the user to input any positive integer
# And outputs the successive values of the following calculation
# At each step calculate the next value by taking current value
# If even divide by 2
# If odd multiply by 3 + 1
# End program if value = 1

# Author: Tosin Araba


def collatz(number):
   
    if (number % 2 == 0): # if number is even
        print(number // 2) # print the number divided by 2
        return number // 2 # return the divided number

    elif (number % 2 == 1): # otherwise if number is odd
        result = number * 3 +1 # multiply the number by 3 and add 1
        print(result) # print the number
        return result

number = int(input("Enter a number: "))
while number != 1: # continue the loop until 1 is returned
    number = collatz(int(number))

