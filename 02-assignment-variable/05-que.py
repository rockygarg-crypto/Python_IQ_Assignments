base_salary = 50000
bonus = 5000
tax_rate = 10 / 100
other_charges = 2000

gross_salary = base_salary + bonus

tax = gross_salary * tax_rate

net_salary = gross_salary - tax_rate - other_charges

print(f"gross_salary : {gross_salary}")
print(f"tax_rate : {tax_rate}")
print(f"net_salary : {net_salary}")
