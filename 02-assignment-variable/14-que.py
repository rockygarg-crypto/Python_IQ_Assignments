#Arranging Three Numbers in Descending Order
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter Third Number : "))

if num1 < num2:
    num1, num2 = num2, num1
if num1 < num3:
    num1, num3 = num3, num1
if num2 < num3:
    num2,num3 = num3, num2

print(f"Number in descending order: {num1, num2,num3}")  
