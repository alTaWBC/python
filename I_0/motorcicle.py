import shelve

with shelve.open(r"I_0\files\bike") as bike:
    bike["mark"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250
    bike["engin_size"] = 250
    for key in bike:
        print(key)

    print()
    print(bike["engine_size"])
    print(bike["engin_size"])

    del bike["engin_size"]
    print()
    for key in bike:
        print(key)

