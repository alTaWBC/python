t = ("a", "b", "c")
print(t)

welcome = "Welcome to my Nightmate", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print()
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)

# Easier to understand than the code form lines 11-14
title, artist, year = metallica
print(title, artist, year, sep="\n")

# Example of tuple confusion
table = ("Coffe Table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)

albums = [
    ("Welcome to my Nightmate", "Alice Cooper", 1975,),
    ("Bad Company", "Bad Company", 1974,),
    ("Nightflight", "Budgie", 1981,),
    ("More Mayhem", "Emilda May", 2011,),
    ("Ride the Lightning", "Metallica", 1984,),
]

print(len(albums))
for (name, artist, year) in albums:
    print(f"Album: {name}, Artist: {artist}, Year: {year}")
