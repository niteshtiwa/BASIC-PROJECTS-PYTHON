import re
pattern = "^hello"
string = "hello , world?"
if re.match(pattern , string):
  print(" pattern matched!")

else:
  print("pattern not matched!")

#2
pattern= r"\bp\w+"
string  = "python is greate! let's learn it "
matches = re.findall(pattern, string)
print("maches found;",matches)

#3
pattern =r"\d+"
string ="my phone number is 123-456-7890"


replaced_string = re.sub(pattern,"#", string)
print(replaced_string)



