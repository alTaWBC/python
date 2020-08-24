options = ["computer", "monitor", "keyboard",
           "mouse", "mouse mat", "computer", "hdmi cable"]
another_list = options

print(id(options))
print(id(another_list))
print()

options += ["cookies"]
print(id(options))
print(id(another_list))

a = b = c = d = e = f = another_list
print(a)
print("Adding Ice Cream")
b += ["Ice Cream"]
print(c)
print(d)

print(a.index("computer", 2, 5))
