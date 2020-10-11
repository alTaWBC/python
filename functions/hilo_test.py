from typing import Dict
LOW = 1
HIGH = 1000

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1


guesses: Dict[int, int] = {}
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    if number_of_guesses not in guesses:
        guesses[number_of_guesses] = 0
    guesses[number_of_guesses] += 1
    print("{} guessed in {}".format(number, number_of_guesses))
print(guesses)


def fizz_buzz(number):
    """Returns Fizz, Buzz, Fizz Buzz or number

    Args:
        number (int): number to check

    Returns:
        [int, str]: Fizz, Buzz, Fizz Buzz or number
    """
    div3 = number % 3 == 0
    div5 = number % 5 == 0
    if not div5 and not div3:
        return number
    if not div5:
        return "fizz"
    if not div3:
        return "buzz"
    return "fizz buzz"
