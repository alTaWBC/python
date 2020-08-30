import shelve

with shelve.open(r'I_0\files\SelfTest') as fruit:
    fruit["orange"] = 'sweet orange'
    fruit["apple"] = 'good for cider'
    fruit["lemon"] = 'sour yellow'
    fruit["grape"] = 'grows in bunches'
    fruit["lime"] = 'sour green'

    print(fruit["lemon"])
    print(fruit["grape"])

    for snack in fruit:
        print(f"{snack}: {fruit[snack]}")
    print()

    for snack in sorted(list(fruit.keys())):
        print(f"{snack}: {fruit[snack]}")

    while True:
        shelf_key = input("please enter a fruit: ")
        if shelf_key == "q":
            break

        print(fruit.get(shelf_key, "Fruit is not in shelf"))

print(fruit)
