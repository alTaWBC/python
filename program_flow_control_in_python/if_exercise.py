name = input("Name? ")
age = int(input("Age? "))

if 18 <= age < 31:
    print(f"Come in {name}")
else:
    print(f"Stop trying to get in {name}!!!!")
