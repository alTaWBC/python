locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small \
brick building",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest"
}

exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    {"N": 5, "Q": 0},
    {"W": 1, "Q": 0},
    {"N": 1, "W": 2, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}
]

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input(f"Available exits are {availableExits}\nYou go? ")\
        .upper()
    if direction not in exits[loc]:
        print("You cannot go in that direction")
    else:
        loc = exits[loc][direction]


# Challenge starts here

exits_dict = {
    0: {"Q": 0},
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
    2: {"N": 5, "Q": 0},
    3: {"W": 1, "Q": 0},
    4: {"N": 1, "W": 2, "Q": 0},
    5: {"W": 2, "S": 1, "Q": 0}
}

options = {
    "WEST": "W",
    "W": "W",
    "NORTH": "N",
    "N": "N",
    "SOUTH": "S",
    "S": "S",
    "EAST": "E",
    "E": "E",
    "Q": "Q",
    "QUIT": "Q",
    "EXIT": "Q"
}

loc = 1
while True:
    availableExits = ", ".join(exits_dict[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = options[input(f"Available exits are {availableExits}\
                              \nYou go? ").upper()]
    if direction not in exits_dict[loc]:
        print("You cannot go in that direction")
    else:
        loc = exits_dict[loc][direction]
