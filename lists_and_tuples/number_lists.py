from typing import List

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
print(max(even))
print(min(even))
print()

print(max(odd))
print(min(odd))
print()

print("mississipi".count("issi"))
print("mississipi".count("iss"))

even.extend(odd)
print(even)
another_even = even
proper_copy = even.copy()
print(another_even)
print(proper_copy)

print()
even.sort(reverse=True)
print(even)
print(another_even)
print(proper_copy)

empty_list: List[str] = []
numbers = even + odd
print()
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

print()
digits = sorted("432985617")
print(list("432985617"))
print(digits)

more_numbers = numbers.copy()    # Same as numbers[:] or list(numbers)
print(numbers is more_numbers)  # They are not the same
print(numbers == more_numbers)  # But they have the same values

nested_lists = [even, odd]
print(numbers)
for number_list in nested_lists:
    print(number_list)
    for number in number_list:
        print(number)
