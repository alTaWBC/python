from typing import Iterable


def func(p1, p2, *args, k, **kwargs):
    print(f"positional-or-keyword: {p1}, {p2}")
    print(f"var-positional(*args): {args}")
    print(f"keywords: {k}")
    print(f"var-keyword (**kwargs): {kwargs}")


func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)


def sum_numbers(*args: Iterable[float]) -> float:
    """Returns the sum of the numbers provided

    Returns:
        Float: Result of sum
    """
    return sum(args)


print(sum_numbers(1, 2))
print(sum_numbers(1, 2, 3, 4, 5, 6))
