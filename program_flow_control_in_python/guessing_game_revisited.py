import random

highest = 10
answer = random.randint(1, highest)
print(answer)  # TODO: Remove
guess = int(input("We need a number: "))

while (guess != answer):
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input("We need a number: "))
else:
    print("Well done you guessed it")
