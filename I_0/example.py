import shelve

s_books = shelve.open(r"I_0\files\books")
books = {
    "recipes": {
        "blt": ["bacon", "lettuce", "tomato", "bread"],
        "beans on toast": ["beans", "bread"],
        "scrambled_eggs": ["eggs", "butter", "milk"],
        "soup": ["tin of soup"],
        "pasta": ["pasta", "cheese"],
    },
    "maintenance": {
        "stuck": ["oil"],
        "loose": ["gaffer tape"],
    }
}

s_books["maintenance"] = books["maintenance"]
s_books["recipes"] = books["recipes"]

print(s_books["recipes"])


s_books.close()
