age = int(input("enter your current age: "))
retirement_age= 65

if age >= retirement_age :
    print("you have already reached retirement age ! ")
else : 
     years_left = retirement_age - age
     print(f"you have {years_left} years left until retirement.")


