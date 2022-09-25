price = float(input("How much was your purchase?"))
mem = input("Are you a member (y/n)?")

if "y" in mem:
    tier = int(input("What membership tier?"))
    if tier == 1:
        price = price - price*.1
    elif tier == 2:
        price = price - price*.2
    elif tier == 3:
        price = price - price*.3
    elif tier == 4:
        price = price - price*.4
    elif tier == 5:
        price = price - price*.5

print(f'{price:.2f}')
