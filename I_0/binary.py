with open(r"I_0\files\binary", "bw") as bin_file:
    bin_file.write(bytes(range(17)))


with open(r"I_0\files\binary", "br") as bin_file:
    for bi in bin_file:
        print(bi)

a = 65534
b = 65535
c = 65536
d = 2998302

with open(r"I_0\files\binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))
    bin_file.write(b.to_bytes(2, "big"))
    bin_file.write(c.to_bytes(4, "big"))
    bin_file.write(d.to_bytes(4, "little"))
    bin_file.write(d.to_bytes(4, "big"))

print()
with open(r"I_0\files\binary2", "br") as bin_file:
    e = int.from_bytes(bin_file.read(2), "big")
    print(e)
    f = int.from_bytes(bin_file.read(2), "big")
    print(f)
    g = int.from_bytes(bin_file.read(4), "big")
    print(g)
    h = int.from_bytes(bin_file.read(4), "big")
    print(h)
    i = int.from_bytes(bin_file.read(4), "little")
    print(i)
