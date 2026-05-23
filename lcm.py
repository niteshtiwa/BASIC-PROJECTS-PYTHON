def lcm(a,b):
    greater = max(a,b)
   while True:
     if greater % a==0 and greater % b==0:
       return greater 
     greater +=1

x = int(input("Enter the first number:")
y= int (intput("Enter the second number:")
print(f"the LCM of {x} and {y} is :{lcm(x,y)}")
        
