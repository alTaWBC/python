from typing import Union


def multiply(x: Union[float, int], y: Union[float, int]) -> float:
    return x * y


print(multiply(2, 3))
for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)


def is_palindrome(palindrome: str) -> bool:
    return palindrome.casefold() == palindrome[::-1].casefold()


def is_palindrome_sentence(palindrome: str) -> bool:
    palindrome = "".join(item if item.isalnum() else "" for item in palindrome)
    print(palindrome)
    return is_palindrome(palindrome)


assert(is_palindrome("aa"))
assert(is_palindrome("aba"))
assert(not is_palindrome("ab"))
assert(is_palindrome("Aba"))
assert(is_palindrome_sentence("a. A"))
assert(is_palindrome_sentence("ola alo"))
assert(is_palindrome_sentence("ola. Alo"))


answer = multiply(18, 3)
print(answer)

# returns nothing


def return_nothing():
    print("hi")


print(return_nothing())
