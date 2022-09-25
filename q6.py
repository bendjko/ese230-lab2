#To-do 6
#Write a function that truncates a non-integer to a given number of decimals. For example, 
#truncating π = 3.141596... to 4 decimals would return 3.1415. Don’t worry about truncating 
#integers. 
import math

def trunc (n, t):
    mult = pow(10, t)
    holder = n*mult
    new = math.trunc(holder)
    return new/mult

num = float(input('What number to truncate?'))
trun = int(input('How many decimal places?'))

truncated = trunc(num,trun)
print(truncated)