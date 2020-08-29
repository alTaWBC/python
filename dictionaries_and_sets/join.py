myList = ["a", "b", "c", "d"]

newString = myList[0]
for c in myList[1:]:
    newString += ", " + c
print(newString)

print()

# use this instead of above
newString = ", ".join(myList)

print(newString)
