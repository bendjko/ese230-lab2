# To do 1: Write a Python code to do exactly what the program in Figure 5 does. 
# Add some statements to take care of the situation where a student enters anything 
# but 1 or 2 when asked what they want to calculate. 
# The program should allow them to re-enter a correct choice.

pi = 3.14159
radius = float(input("Enter the radius of the sphere: "))

print("To calculate surface area, enter 1")
print("To calculate volume, enter 2")

quantity = int(input("What do you want to calculate? "))

if quantity != 1 or quantity != 2:
    print("Invalid input, please choose 1 or 2")
    quantity = int(input("What do you want to calculate? "))
if quantity == 1:
    surface_area = 4 * pi * radius ** 2
    print("The surface area is ", surface_area)
elif quantity == 2:
    volume = (4 * pi * radius * radius * radius)/ 3
    print("The sphere volume is", volume)


