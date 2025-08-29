import random

print("Hi there! I'm going to try to guess your age.")

name = input("Please input your name:  ")

guessed_correctly = False

while not guessed_correctly:
    guess = random.randint(15, 30)
    answer = input(f"Are you {guess} years old? (y/n): ").lower()
    
    if answer == 'y':
        print(f"Awesome! {name} is {guess} years old.")
        guessed_correctly = True
    else:
        print("Dang it.")