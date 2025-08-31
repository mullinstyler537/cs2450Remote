import random

print("Hi! I'm going to try to guess your age.")

name = input("First, what's your name? ")

while True:
    guess = random.randint(15, 30)
    answer = input(f"Is your age {guess}? (y/n): ").lower()
    if answer == 'y':
        print(f"Awesome! {name} is {guess} years old.")
        break
    else:
        print("Dang it.")
