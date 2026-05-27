text = input("enter a stirng:")
vowels= "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f" The number of vowels in the string is:{count}")