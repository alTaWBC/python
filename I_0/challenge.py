
with open(r"I_0\files\sample.txt", "a") as jabber:
    print("\n", file=jabber)
    for i in range(1, 13):
        print(f"{i:>2} times 2 is {i*2:<2}", file=jabber)
