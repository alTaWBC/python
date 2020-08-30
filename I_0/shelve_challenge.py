# Modify the program from the Second Dictionary challenge of lecture 56
# to use shelves instead of dictionaries.
#
# Do this by creating two programs. cave_initialise.py should create the two
# shelves (locations and vocabulary) with the appropriate keys and values.
#
# cave_game.py will then use the two shelves instead of dictionaries.
# Apart from opening and closing the shelves, cave_game will need only
# two changes to the actual code - remember that shelf keys MUST be strings!
#
# Just to be clear, cave_game.py will contain the code from line 45, everything
# before that (modified to use shelves) will be in cave_initialise.py.

import shelve

location_shelf = shelve.open(r"I_0\files\locations")

location_shelf["0"] = {"desc": "You are sitting in front of a\
computer learning Python",
                       "exits": {},
                       "namedExits": {}}

location_shelf["1"] = {"desc": "You are standing at the end of a\
road before a small brick building",
                       "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                       "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}}

location_shelf["2"] = {"desc": "You are at the top of a hill",
                       "exits": {"N": 5, "Q": 0},
                       "namedExits": {"5": 5}}

location_shelf["3"] = {"desc": "You are inside a building,\
a well house for a small stream",
                       "exits": {"W": 1, "Q": 0},
                       "namedExits": {"1": 1}}

location_shelf["4"] = {"desc": "You are in a valley beside a stream",
                       "exits": {"N": 1, "W": 2, "Q": 0},
                       "namedExits": {"1": 1, "2": 2}}

location_shelf["5"] = {"desc": "You are in the forest",
                       "exits": {"W": 2, "S": 1, "Q": 0},
                       "namedExits": {"2": 2, "1": 1}}

vocabulary_shelf = shelve.open(r"I_0\files\vocabulary")

vocabulary_shelf["QUIT"] = "Q"
vocabulary_shelf["NORTH"] = "N"
vocabulary_shelf["SOUTH"] = "S"
vocabulary_shelf["EAST"] = "E"
vocabulary_shelf["WEST"] = "W"
vocabulary_shelf["ROAD"] = "1"
vocabulary_shelf["HILL"] = "2"
vocabulary_shelf["BUILDING"] = "3"
vocabulary_shelf["VALLEY"] = "4"
vocabulary_shelf["FOREST"] = "5"


loc = "1"
while True:
    availableExits = ", ".join(location_shelf[loc]["exits"].keys())

    print(location_shelf[loc]["desc"])

    if loc == "0":
        break
    else:
        allExits = location_shelf[loc]["exits"].copy()
        allExits.update(location_shelf[loc]["namedExits"])

    direction = input("Available exits are " + availableExits).upper()
    print()

    # Parse the user input, using our vocabulary dictionary if necessary
    if len(direction) > 1:  # more than 1 letter, so check vocab
        words = direction.split()
        for word in words:
            # does it contain a word we know?
            if word in vocabulary_shelf.keys():
                direction = vocabulary_shelf[word]
                break

    if direction in allExits:
        loc = str(allExits[direction])
    else:
        print("You cannot go in that direction")


vocabulary_shelf.close()
location_shelf.close()
