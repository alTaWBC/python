low = 1
high = 1000
count = 1

print(f"Please insert a number between {low} and {high}: ")

while low != high:
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess} is it higher \
(h), lower(l) or correct (c)?").casefold()

    if high_low == "c":
        print(f"I got it in {count} guesses")
        break
    elif high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = max(guess - 1, 1)
    else:
        print("You need to insert h for higher, l for lower or c for correct")
        continue
    count += 1
else:
    print(f"The correct number is {low}")
    print(f"I got it in {count} guesses")
