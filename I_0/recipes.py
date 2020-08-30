import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]


# Only way to add information to shelves
with shelve.open(r"I_0\files\recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["soup"] = soup
    recipes["pasta"] = pasta

    temp_list = recipes["pasta"]
    temp_list.append("tomato")
    recipes["pasta"] = temp_list
    temp_list = recipes["blt"]
    temp_list.append("butter")
    recipes["blt"] = temp_list

    for food in recipes:
        print(food, recipes[food])
    print("="*40)

pancakes = ["milk", "eggs"]
# Way to allow changes to shelves
with shelve.open(r"I_0\files\recipes", writeback=True) as recipes:
    recipes["soup"].append("salt")
    recipes["pancakes"] = pancakes
    recipes.sync()  # This line forces the changes to be written in memory
    # If we comment line above this change is written in the shelf.
    # If we leave the line above peanut butter is not written in the shelf
    pancakes.append("peanut butter")

    for food in recipes:
        print(food, recipes[food])
