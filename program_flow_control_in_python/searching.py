shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

for i in range(len(shopping_list)):
    print(i)
    if shopping_list[i] == item_to_find:
        found_at = i
        break

if found_at is not None:
    print(f"Item found at position {found_at}")
else:
    print(f"{item_to_find} not found")
