# My solution to weekly task 02

# program that calculates BMI
# The inputs are height in centimetres and weight in kilograms
# The output is BMI
# Author: Tosin Araba

# BMI = weight (kg)/height(m)2
# height = 180cm weight = 65kg

Height = int(input("Enter height in centimetres: "))
Weight = int(input("Enter weight in kilogram: "))
heightInMetres = Height/100
heightInMetresSquared = heightInMetres**2
BMI = round(Weight/heightInMetresSquared, 2)

print("The BMI is {}".format(BMI))
