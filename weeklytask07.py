# Answer to weekly task 7
# program that reads in a text file and outputs the number of e's it contains

#Author: Tosin Araba

def letterFrequency(fileName, letter): 
    #open file in read mode
    file = open(fileName, 'r')

    #store content of the file in a variable
    text = file.read()

    #using count()
    return text.count(letter)


#call the function and return the letter count
print(letterFrequency('myfile.txt', 'e'))