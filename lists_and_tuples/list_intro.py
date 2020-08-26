options = ["computer", "monitor", "keyboard",
           "mouse", "mouse mat", "hdmi cable"]

for part in options:
    print(part)

print()
print(options[2])
print(options[0:3])
print(options[-1])

print()
options[3:] = "trackball"
print(options)
options[3:] = ["trackball"]
print(options)
