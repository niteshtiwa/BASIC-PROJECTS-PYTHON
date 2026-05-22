number1= int(input("Enter the first  number"))
number2= int (input("Enter the second number"))
number3= int(input("Enter the third number"))
if number1>number2:
  number1,number2= number2, number1
if number1>number3:
  number1, number3= number3, number1
if number2>number3:
  number2, number3= number3, number2
print(" Sorted numbers:", number1, number2, number3)
