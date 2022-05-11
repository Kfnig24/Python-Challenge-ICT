import math

a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
q = math.floor(a / b)
r = int(math.remainder(a, b))

print("Quotient:", q)
print("Remainder", r)