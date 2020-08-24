age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print(f"You can't work with {age} years")

print("-" * 50)

if age < 16 or age > 65:
    print(f"You can't work with {age} years")
else:
    print("Have a good day at work")

if age in range(16, 66):
    print(f"You can't work with {age} years")
else:
    print("Have a good day at work")

