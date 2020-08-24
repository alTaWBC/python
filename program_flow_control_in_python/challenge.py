options = """Please choose your option from the list below:
1. Learn Python
2. Learn Java
3. Go swimming
4. Have dinner
5. Go to bed
0. Exit"""

option = ""
while option != "0":
    if option == "1":
        print("You learned Python")
    elif option == "2":
        print("You learned Java")
    elif option == "3":
        print("You went swimming")
    elif option == "4":
        print("You had dinner")
    elif option == "5":
        print("zzzzzzzz")
    else:
        print(options)
    option = input("Please choose an option from the menu: ").casefold()
else:
    print("Have a nice day")
