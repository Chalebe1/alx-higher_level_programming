#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print(number)
if (number % 10 > 5 ):
    print(f"The last digit of {number:d} is {number % 10:d} and is greater than 5")

if (number % 10 == 0 ):
    print(f"The last digit of {number:d} is {number % 10:d} and is 0")

if ((number % 10 < 6) and (number % 10 != 0)):
    print(f"The last digit of {number:d} is {number % 10:d} and is less than 6 and not 0")
print("\n")

