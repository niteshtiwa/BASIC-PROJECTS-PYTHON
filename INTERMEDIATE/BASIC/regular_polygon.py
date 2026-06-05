import math
n=int (input("Please enter the number of the sides:"))
s = int (input("please enter the length of the side: "))
area = (n * s**2)/ (4*math.tan(math.pi/n))

# output the result
print(f"The area  of the polygon is : {area:.3f}")