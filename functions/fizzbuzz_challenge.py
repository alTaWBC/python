

def fizz_buzz(number: int) -> str:
    """Returns Fizz, Buzz, Fizz Buzz or number

    Args:
        number (int): number to check

    Returns:
        [int, str]: Fizz, Buzz, Fizz Buzz or number
    """
    div3 = number % 3 == 0
    div5 = number % 5 == 0
    if not div5 and not div3:
        return str(number)
    if not div5:
        return "fizz"
    if not div3:
        return "buzz"
    return "fizz buzz"


next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = correct_answer  # input("Your go: ")
    if players_answer != correct_answer:
        print(f"Loser! {correct_answer} was the correct answer")
        break
else:
    print("Well Done")


def factorial(number: int) -> int:
    """Returns factorial of number

    Args:
        number (int): number 

    Returns:
        int: factorial of number
    """
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

