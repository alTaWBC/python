parrot = "Norwegian Blue"

print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[-4:])

print(parrot[0:9:2])
print(parrot[3:5], parrot[3:9:3])

number = "9,223;372:036 854,775;807"
separators = number[1::4]
values = ("".join(char if char not in separators else " " for char in number)
          .split())
print([int(val) for val in values])

print(parrot[::-1])

alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[-10:-13:-1])
print(alphabet[4::-1])
print(alphabet[:-9:-1])

