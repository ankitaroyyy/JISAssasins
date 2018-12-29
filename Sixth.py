#19
print("Enter the sides of a triangle")
x = int(input("Enter first side"))
y = int(input("Enter second side"))
z = int(input("Enter third side"))
if (x+y>z) and (x+z>y) and (z+y>x):
    print("Triangle is valid")
else:
    print("Invalid Triangle")