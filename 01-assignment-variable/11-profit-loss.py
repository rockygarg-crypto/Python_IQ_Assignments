cost_price = 500
selling_price = 600
print(f"cost_price : {cost_price}")
print(f"selling_price : {selling_price}")

percentage = ((selling_price - cost_price) / cost_price) *100
print(f"profit loss percentage : {percentage}%")
if selling_price > cost_price:
    print("profit")
    print("loss")
