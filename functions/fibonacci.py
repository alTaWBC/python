def fibonacci(nth_fibonacci: int, first=0, second=1) -> int:
    """Returns the nth value of fibonacci sequence starting in values first, second

    Args:
        nth_fibonacci (int): number to determine
        first (int, optional): value to start. Defaults to 0.
        second (int, optional): value to start. Defaults to 1.

    Returns:
        int: nth value of fibonacci sequence
    """
    value = min(nth_fibonacci, second)
    for _ in range(1, nth_fibonacci):
        value = first + second
        first = second
        second = value
    return value


for i in range(36):
    print(i, fibonacci(i))
