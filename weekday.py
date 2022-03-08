# solution to weekly task 5

# Program that outputs whether or today is a weekday

# Author: Tosin Araba

import datetime

weekno = datetime.datetime.today().weekday()
if weekno < 5:
    print("yes, unfortunately today is a weekday")
else: # 5 Sat, 6 Sun
    print("it is the weekday, yay!")
    
