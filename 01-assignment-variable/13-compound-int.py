principal = 10000
rate = 5
time = 2
print(f"principal : {principal}")
print(f"rate : {rate}")
print(f"time : {time}")
CI =int(principal * (1 + rate / 100) ** time - principal)
print(f"compound interest : {CI}")

