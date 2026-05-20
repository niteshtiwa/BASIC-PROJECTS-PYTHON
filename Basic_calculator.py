# display the calculator menu
print("Welcome to the basic Calculator")
print ("1. Addition")
print ("2. Substraction")
print ("3. Devision")
print("4. Multiplication")

# get the users choice
choice= input(" choose an operation from (1/2/3/4):")

 # Get two numbers from the user
num1= float(input("enter the first number:"))
num2= float(input("enter the second number:"))
# perform the choosen operation
if choice =="1":
  print(f"the result of addition : {num1+num2}")
elif choice =="2":
  print(f"the result of the substraction : {num1-num2}")
elif choice =="3":
   if num2!= 0:
    print (f" the result of the devision {num1 /num2}")
   else :
        print("Error: devision is not possible")
elif choice =="4":
  print(f" the result of the multiplication {num1*num2}")

else :
  print(" invalid Choice. Please select the correct choice")