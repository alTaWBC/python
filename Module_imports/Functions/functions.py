def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" "*left_margin, text)


def centre_text(*args, sep=" ", end='\n', flush=False, file=None):
    """ Prints text centered

    Args:
        text ([string, int]): Text to print
    """
    text = sep.join(str(item) for item in args)
    left_margin = (80 - len(text)) // 2
    print(" "*left_margin, text, end=end, flush=False, file=file)


# call the function
python_food()
centre_text("spam")
centre_text("spam, spam")
centre_text(12, 13, 14, 15)
centre_text(12, 13, 14, 15, sep=', ')

with open(r"Module_imports\Functions\center.txt", mode="w") as centered_file:
    centre_text(12, 13, 14, 15, 16, file=centered_file)
