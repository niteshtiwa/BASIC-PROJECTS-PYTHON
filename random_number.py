import random 
low = int(input("Enter the lower number :"))
high= int(input("Enter the upper bound:"))

random_num= random.randint(low, high,6) # it will generate the 6 random number between them 
print(f"Random number between {low} and {high}:{random_num}")
