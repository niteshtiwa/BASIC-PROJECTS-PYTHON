import random
# Generate a random number between 1 and 100
secret_number = random.randint(1,100)
print("Welcome to the Number guessing game !")
print(" i have chosen number 1 and 100, can you guess it?")
attempts =0
while True:
  # GEt the user's guess
  guess = input("Enter your guess(or type 'quit' to exit):")
  if guess.lower()=='quit':
     print(f"you gave up!  The secret number was{secret_number}, ")
     break
  try: 
     guess = int (guess)
  except ValueError:
     print(' please enter a valid number.')
     continue
  attempts+=1
  if guess == secret_number:
     print(f"Congratulations! you guessed the number in {attempts}.")
     break
  elif guess < secret_number:
     print('Too low! try again')
  elif guess > secret_number:
     print('Too high! try again')