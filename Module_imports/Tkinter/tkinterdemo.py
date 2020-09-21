import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()  # type: ignore

mainWindow = tkinter.Tk()

width = '640'
height = '640'
left_margin = '100'
top_margin = '50'
geom = f"{width}x{height}+{left_margin}+{top_margin}"

mainWindow.title("Hello World!")
mainWindow.geometry(geom)

label = tkinter.Label(mainWindow, text="Hello World")

# The code below uses pack
# label.pack(side='top')

# left_frame = tkinter.Frame(mainWindow)
# left_frame.pack(side="left", anchor='n', fill=tkinter.Y, expand=False)

# canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
# canvas.pack(side='left', anchor='n')
# # Options include fill=tkinter.(BOTH or X or Y), add expand=True if
# # it is not expanding

# right_frame = tkinter.Frame(mainWindow)
# right_frame.pack(side="right", anchor='n', fill=tkinter.Y, expand=True)

# button1 = tkinter.Button(right_frame, text="Button1")
# button2 = tkinter.Button(right_frame, text="Button2")
# button3 = tkinter.Button(right_frame, text="Button3")

# button1.pack(side="top", anchor='n')
# button2.pack(side="top", anchor='s')
# button3.pack(side="top", anchor='e')


# The code below uses grid
label.grid(row=0, column=0)

left_frame = tkinter.Frame(mainWindow)
left_frame.grid(row=1, column=1)

canvas = tkinter.Canvas(left_frame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

right_frame = tkinter.Frame(mainWindow)
right_frame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(right_frame, text="Button1")
button2 = tkinter.Button(right_frame, text="Button2")
button3 = tkinter.Button(right_frame, text="Button3")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

left_frame.config(relief='sunken', borderwidth=1)
right_frame.config(relief='sunken', borderwidth=1)

left_frame.grid(sticky='ns')
right_frame.grid(sticky='new')

right_frame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop()
