cities = ["Adelaide", "Braga", "Porto", "Darwing", "Jonesis"]

with open("I_0\filescities.txt", "w") as city_file:
    for city in cities:
        print(city, file=city_file)

cities.clear()
with open("I_0\filescities.txt", "r") as city_file:
    for city in city_file:
        cities.append(city.strip())
        print(city.strip())
print(cities)

imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"))

with open(r"I_0\files\imelda.txt", "w") as imelda_file:
    print(imelda, file=imelda_file)

with open(r"I_0\files\imelda.txt", "r") as imelda_file:
    contents = imelda_file.readline().strip()

print(contents)
imelda = eval(contents)
print(imelda)
print(imelda[1])
print(contents[2])
