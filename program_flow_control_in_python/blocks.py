for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*"*50)

name = input("Please enter your name: ")
age = int(input("How old are you {}? ".format(name)))
print(age)

if age >= 18:
    print(f"You can vote {name}")
    print("Please put an X in the box")
else:
    print(f"You aren't old enough to vote {name}, \
         you can vote in {18-age} years")

if age < 18:
    print(f"You aren't old enough to vote {name}, \
         you can vote in {18-age} years")
elif age == 900:
    print("Sorry Yoda, you die in Return of the Jedi")
else:
    print(f"You can vote {name}")
    print("Please put an X in the box")
