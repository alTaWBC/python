farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)
print("="*40)

wild_animals = set(["lion", "tiger", "panther"])
print(wild_animals)

for animal in wild_animals:
    print(animal)
print("="*40)

farm_animals.add("horse")
wild_animals.add("elephant")
print()

print(farm_animals)
print(wild_animals)

empty_set = set()
empty_set_2 = {}  # type:ignore
empty_set.add("a")
# empty_set_2.add ("b") Cannot be used in dictionaries

even = set(range(0, 40, 2))
print("Even: ", even)

odd_tuples = (1, 3, 5, 7, 9)
odd = set(odd_tuples)
print("Odd: ", odd)

squares = set([4, 9, 16, 25])
print("Squares: ", squares)

print(even.union(odd))
print("Union:", even.union(squares))
print(f"""Even: {len(even)}
Squares: {len(squares)}
Union: {len(even.union(squares))}""")

print("Difference: ", even.difference(squares))
print("Same: ", even.intersection(squares))

# Functions above return result
# Functions below enforce result on variable

even.intersection_update(squares)
print("Even after intersection: ", even)
print()
print(squares.symmetric_difference(even))
print(even.symmetric_difference(squares))
print()
print(squares.difference(even))
print(even.difference(squares))

squares.remove(4)
squares.discard(25)
squares.discard(8)  # Does not give error
# squares.remove(8) Gives error
print("Squares: ", squares)

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print("Squares is subset of even")

if squares.issuperset(even):
    print("Squares is superset of even")

frozen_even = frozenset(range(0, 100, 2))  # Cannot be changed
print(frozen_even)
# frozen_even.add(3) Impossible
