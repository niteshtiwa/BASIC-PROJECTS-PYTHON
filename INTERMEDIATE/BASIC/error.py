# try 
# except  
# else 
# finally
try:
  numerator = int(input("enter a numberaot:"))
  denominator = int (input("enter denominator:"))
  result = numerator/denominator
except  ZeroDivisionError:
  print("Error: you can't devide by the zero")
except ValueError:
  print("Error: enter the valid value")
else: 
  print(f"result: {result}")
finally :
  print("Execution completed!")



