
days = int(input("Enter number of days : "))

if days <= 5 :
    charge = days * 2
    print(f"Calculated : {charge}")
elif days >= 6 and days <= 10 :
    charge = days * 3
    print(f"Calculated : {charge}")
elif days >= 11 and days <=15 :
    charge = days * 4
    print(f"Calculated : {charge}")
else :
    charge = days * 5
    print(f"Calculated : {charge}")