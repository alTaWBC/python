import tkinter

list_of_buttons = [
    ("C", 1, 0, 1),
    ("CE", 1, 1, 1),
    ("7", 2, 0, 1),
    ("8", 2, 1, 1),
    ("9", 2, 2, 1),
    ("+", 2, 3, 1),
    ("4", 3, 0, 1),
    ("5", 3, 1, 1),
    ("6", 3, 2, 1),
    ("-", 3, 3, 1),
    ("1", 4, 0, 1),
    ("2", 4, 1, 1),
    ("3", 4, 2, 1),
    ("*", 4, 3, 1),
    ("0", 5, 0, 1),
    ("=", 5, 1, 2),
    ("/", 5, 3, 1),
]


mainWindow = tkinter.Tk()

width = '640'
height = '640'
left_margin = '100'
top_margin = '50'
geom = f"{width}x{height}+{left_margin}+{top_margin}"

mainWindow.title("Hello World!")
mainWindow.geometry(geom)

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4)
result.set

for button in list_of_buttons:
    button_widget = tkinter.Button(mainWindow, text=button[0])
    button_widget.grid(row=button[1], sticky='ew',
                       column=button[2], columnspan=button[3])


# mainWindow.minsize(geom)
mainWindow.mainloop()
