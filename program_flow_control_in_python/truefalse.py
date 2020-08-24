day = "Saturday"
temperature = 30
raining = True

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

if 0:
    print("True")
else:
    print("False")

name = input("Please type your name: ")
if name:
    print(f"Hello, {name}")
else:
    print("Are you the name with no name?")
