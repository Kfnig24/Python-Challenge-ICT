number = int(input("Enter a number: "))

if number == 1:
  c = int(input("Enter the length of the side: "))
  print(c*c, "cm2")
elif number == 2:
  h = int(input("Enter the height of the triangle: "))
  b = int(input("Enter the base of the triangle: "))
  print((h*b)/2, "cm2")
else:
  print("You pick a wrong number.")