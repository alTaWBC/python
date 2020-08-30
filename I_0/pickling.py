import pickle

imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open(r"I_0\files\imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(odd, pickle_file)

with open(r"I_0\files\imelda.pickle", "rb") as pickle_file:
    imelda = pickle.load(pickle_file)
    even = pickle.load(pickle_file)
    odd = pickle.load(pickle_file)

print(imelda, type(imelda))
print(even, type(even))
print(odd, type(odd))
