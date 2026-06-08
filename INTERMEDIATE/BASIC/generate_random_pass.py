import string 
import random 
length = int(input("Enter the password length:"))
characters= string.ascii_letters +string.digits+ string.puncuation
password =''.join(random.choices(characters,k=length))
print(f"Genrated password: {password}")