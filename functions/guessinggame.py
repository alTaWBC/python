answer = 5


def get_integer(prompt: str) -> int:
    """Creates a banner where text is centered

    Args:
        text (str, optional): Text to center. Defaults to " ".
        screen_width (int, optional): size of banner. Defaults to 80.

    Raises:
        ValueError: len(text) is larger than width
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print(temp, "is not a valid number")


prompt = "Please guess number between 1 and 10: "
guess = get_integer(prompt)

if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = get_integer("another guess: ")
    if guess == answer:
        print("Well done you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
