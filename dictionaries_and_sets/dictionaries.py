fruit = {
    "orange": "a sweet orange",
    "apple": "good for cider",
    "lemon": "sour",
    "grape": "grows in bunches",
    "lime": "sour and green"
}

print(fruit)
print(fruit["lemon"])
fruit["pear"] = "an odd shaped apple"
print(fruit["pear"])
fruit["pear"] = "great with tequila"
print(fruit["pear"])
del fruit["lemon"]

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     # elif dict_key in fruit:
#     #     print(fruit[dict_key])
#     # else:
#     #     print("Fruit not in dictionary")

#     # Same as above
#     print(fruit.get(dict_key, "Fruit not in dictionary"))

print()
for snack in fruit:
    print(snack, fruit[snack], sep='\t')

print()
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for f in ordered_keys:
    print(f, fruit[f], sep='\t')

# same as above
print()
for f in sorted(list(fruit.keys())):
    print(f, fruit[f], sep='\t')

# same as above but is less efficient
print()
for f in fruit.values():
    print(f)

# fruit.clear()
# print(fruit)


print(fruit.items())
print()
f_tuple = fruit.items()
print(f_tuple)

for s_tuple in f_tuple:
    # print(item, " is ", description)
    item, description = s_tuple
    print(" is ".join([item, description]))

print(dict(f_tuple))
