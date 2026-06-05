n= int(input("Enter the number of the terms:"))
f1,f2=0,1
print("Fibonacci seqence:")
for _ in range(n):
  print(f1,end=" 5")
  f1,f2=f2,f1+f2
