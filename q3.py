# To do 3: Write a Python code using a while loop. 
# The program should repeatedly ask the user to enter an integer until the user inputs the letter q. 
# The program should then output the sum of the integers entered.

sum = 0
inputInt = input("Enter an integer: ")

while inputInt != "q": 
    sum += int(inputInt)
    inputInt = input("Enter an integer: ")

print(sum)