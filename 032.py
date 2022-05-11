import math

radius = int(input("Enter the radius of the cylinder : "))
area = math.pi * math.pow(radius, 2)
depth = int(input("Enter the depth of the cylinder : "))
volume = area * depth
rounded = (math.floor(volume * 1000)) / 1000
print(rounded, "cm2")