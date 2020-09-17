import shelve
print(dir())
print(dir("__bultins__"))

for m in dir("__bultins__"):
    print(m)

print()
print(dir())

for objects in dir(shelve.Shelf):
    print(objects)


print("*"*40)
for objects in dir(shelve.Shelf):
    if objects[0] != '_':
        print(objects)
