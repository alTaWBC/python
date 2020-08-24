number = "9,223;372:036 854,775;807"
separators = number[1::4]
values = ("".join(char if char not in separators else " " for char in number)
          .split())
print([int(val) for val in values])

number = input("Need number: ")
separators = ""
for char in number:
    if not char.isnumeric():
        separators += char

print(separators)
