fruit = {
    "orange": "a sweet orange",
    "apple": "good for cider",
    "lemon": "sour",
    "grape": "grows in bunches",
    "lime": "sour and green"
}

print(fruit)

vegetable = {
    "cabbage": "every child's favorite",
    "sprouts": "mmm, lovely",
    "spinach": "Can I have fruit instead?"
}

# print(vegetable)
# vegetable.update(fruit)
# print(vegetable)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(vegetable)
print()
print(nice_and_nasty)
