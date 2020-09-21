import tkinter
import os

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

label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
for zone in os.listdir('/Windows/System32'):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(
    mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

option_frame = tkinter.LabelFrame(mainWindow, text="File Details")
option_frame.grid(row=1, column=1, sticky='ne')
rbValue = tkinter.IntVar()
rbValue.set(3)

# radio buttons
radio1 = tkinter.Radiobutton(
    option_frame, text='Filename', value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(
    option_frame, text='Path', value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(
    option_frame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# Displays result
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')
hourSpinner = tkinter.Spinbox(timeFrame, width=2, value=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
minuteSpinner.grid(row=0, column=2)
secondpinner.grid(row=0, column=4)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
timeFrame['padx'] = 36

dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
dayLabel = tkinter.Label(dateFrame, text='Day')
monLabel = tkinter.Label(dateFrame, text='Month')
yeaLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monLabel.grid(row=0, column=1, sticky='w')
yeaLabel.grid(row=0, column=2, sticky='w')
daySpinner = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monSpinner = tkinter.Spinbox(dateFrame, width=5, from_=1, to=12)
yeaSpinner = tkinter.Spinbox(dateFrame, width=5, from_=1975, to=2020)
daySpinner.grid(row=1, column=0)
monSpinner.grid(row=1, column=1)
yeaSpinner.grid(row=1, column=2)

# Buttons
okButton = tkinter.Button(mainWindow, text='OK')
cancelButton = tkinter.Button(
    mainWindow, text='Cancel', command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()
