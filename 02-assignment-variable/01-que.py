cost_price = int(input("enter the cost price: "))
selling_price = int(input("enter the selling price: "))
if selling_price > cost_price :
   profit = selling_price - cost_price
   print(f"profit = {profit}")
   profit_percentage = (profit / cost_price) * 100
   print(f"profit_percentage : {profit_percentage}%")
elif cost_price > selling_price :
   loss = cost_price - selling_price
   print(f"loss = {loss}")
   loss_percentage = (loss / cost_price) * 100
   print(f"loss_percentage : {loss_percentage}%")








