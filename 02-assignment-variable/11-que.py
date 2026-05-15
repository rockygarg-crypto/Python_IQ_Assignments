employee_name = input("Enter your name : ")
employee_id = int(input("Enter you ID :"))
employee_exp = int(input("Enter your experience :"))
if employee_exp >= 10 :
    salary = 80000
    print(f"""Senior Employee 
Salary : {salary}""")
    if employee_exp >= 15 :
       salary = salary + 5000
       print(f"""Experience exceeds more than 15 years Bonus added
Salary : {salary}""")

elif employee_exp >= 5 and employee_exp <= 9 :
    salary = 50000
    print(f"""Mid-level Employee
Salary : {salary}""")