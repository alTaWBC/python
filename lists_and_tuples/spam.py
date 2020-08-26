menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item)
    else:
        print(f"{meal} has a spam score of {meal.count('spam')}")
print()

# Removing Spam
# Printing
for meal in menu:
    items = []
    for item in meal:
        if item != "spam":
            items.append(item)
    print(items)
print()

# Cleaner way to print but with comma in the end
for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()
print()

# Cleaner way to print
for meal in menu:
    meal_items = ", ".join((item for item in meal if item != "spam"))
    print(meal_items)
print()

for meal in menu:
    print(", ".join(meal))
print()

# Deleting from list
for meal in menu:
    top_index = len(meal) - 1
    for index, value in enumerate(reversed(meal)):
        if value == "spam":
            del meal[top_index - index]
    print(meal)
