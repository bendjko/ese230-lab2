# To do 4: Write a function that approximates Euler’s number e = 2.71828... using its Taylor Series. 
# The program should prompt the user for an integer that tells it how many numbers to sum in the series.

import math

def approximate_eulers_no(n):
    e = 0
    for i in range(n):
        e += 1/math.factorial(i)
    return e    

n = int(input("Enter an integer: "))
print(approximate_eulers_no(n))
