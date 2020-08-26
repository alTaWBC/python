panagram = """The quick brown
fox jumps\tover
the lazy fox"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

g_list = [
    "9", ' ',
    '2', '2', '3', ' ',
    '3', '7', '2', ' ',
    '0', '3', '6', ' ',
    '8', '5', '4', ' ',
    '7', '7', '5', ' ',
    '8', '0', '7',
]

values = "".join(g_list)
print(values)

values_list = values.split()
print(values_list)

g_int_list = []
for value in values_list:
    if value.isdigit():
        g_int_list.append(int(value))
print(g_int_list)
