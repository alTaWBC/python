result = True
another_result = result
print(id(result))
print(id(another_result))

result = False
print(id(result))
print(id(another_result))

print()
s_result = "Correct"
s_another_result = result
print(id(s_result))
print(id(s_another_result))

s_result += "False"
print(id(s_result))
print(id(s_another_result))
