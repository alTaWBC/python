pangram = "The quick brown fox jumps over the lazy dog"
letter = sorted(pangram)
print(letter)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

# Don't use the code below
another_sorted_numbers = numbers.sort()  # type: ignore
print(numbers)
print(another_sorted_numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)

case_insensitive_sorted = sorted(pangram, key=str.casefold)

names = ["Graham", "John", "terry", "eric", "Terry", "michael"]
names.sort(key=str.casefold)
print(names)
