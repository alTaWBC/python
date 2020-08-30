jabber = open(r"I_0\files\sample.txt", 'r')
# Don't forget the r"" to ignore slashes

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()
print()

# Same as above but preferred
with open(r"I_0\files\sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')
print()

# Same as above
with open(r"I_0\files\sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        if "JAB" in line.upper():
            print(line, end='')
        line = jabber.readline()

# Same as above
with open(r"I_0\files\sample.txt", 'r') as jabber:
    lines = jabber.readlines()
    # print(lines)
print()

for line in lines:
    if "JAB" in line.upper():
        print(line, end='')
print()

# Some possibilities
for line in lines[::-1]:
    if "JAB" in line.upper():
        print(line, end='')




