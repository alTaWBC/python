# phrase = input("Just input something:\n")
# print("Nice you can type\nYou can pat yourself in your back")

phrase = "The quick brown fox jumps over the lazy dog"
vowels = frozenset("aeiou")
forbidden_characters = frozenset(" ;,.:-_~^")

result = set(phrase).difference(vowels).difference(forbidden_characters)
print(sorted(result, key=str.casefold))