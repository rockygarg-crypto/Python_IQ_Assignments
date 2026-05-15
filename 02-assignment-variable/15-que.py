#Tax Calculation for Car Purchase

brand = input("Enter Car Brand : ")
price = int(input("Enter car price in Lakhs : "))

if brand == "Mahindra" and price >= 7 and price <= 10:
    tax = 5
    car_tax = (price*tax)/100
    print(f"Tax on purchase  in lakhs: {car_tax}")
elif brand == "Audi" and price >= 10 and price <= 15:
    tax = 10
    car_tax = (price*tax)/100
    print(f"Tax on purchase in lakhs : {car_tax}")
elif brand == "Jaguar" and price >= 15 and price <= 20:
    tax = 25
    car_tax = (price*tax)/100
    print(f"tax on car purchase in lakhs : {car_tax}")
elif brand == "Mercedes" and price >= 20 and price <= 25:
    tax = 30
    car_tax = (price*tax)/100
    print(f"tax on car purchase in lakhs : {car_tax}") 