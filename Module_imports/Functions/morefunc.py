import tkinter
# import math as m


def parabola(page, size):
    for x in range(-size, size):
        y = x**2/size
        plot(page, x, y)


def circle(page, radius, g, h, color="red"):
    page.create_oval(g+radius, h+radius, g-radius,
                     h-radius, outline=color, width=2)

    # Same as above
    # for x in range(g * 100, (g+radius) * 100):
    #     x /= 100
    #     y = h + (m.sqrt(radius**2 - ((x-g)**2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axis(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(page, x, y):
    page.create_line(x, -y, x+1, -y-1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axis(canvas)

parabola(canvas, 100)
parabola(canvas, 200)

circle(canvas, 100, 100, 100)
circle(canvas, 100, 100, -100)
circle(canvas, 100, -100, 100)
circle(canvas, 100, -100, -100, color='green')

mainWindow.mainloop()
