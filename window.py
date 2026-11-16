
from tkinter import *
import serial
import datetime
import os
import time

myPort = "COM3"

arduino = serial.Serial(port="COM3", baudrate=9600, timeout=.1)
do_write = False


def startReading():
    global do_write

    file = userfile.get()

    if not file:
        label.config(text="Please enter a file name")
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    with open(file, 'w', encoding="utf-8") as f:
        f.write(f'Recording started: {timestamp}\n')

    do_write = True
    startButton.config(text='Reading')

    refresh()


def updatedState():
    if do_write:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        data = arduino.readline().decode('utf-8').strip()

        if data:
            label.config(text=data)

            with open(userfile.get(), 'a', encoding="utf-8") as f:
                f.write(timestamp + ' ' + data + '\n')

    root.after(50, updatedState)


def refresh():
    if do_write:
        updatedState()


# Start GUI
root = Tk()

entryLabel = Label(root, text="File Name:")
entryLabel.pack()

userfile = Entry(root, width=40)
userfile.pack()

startButton = Button(root, text="Start", command=startReading)
startButton.pack(pady=5)

label = Label(
    root,
    text="Waiting for Arduino...",
    bg="#000000",
    height=4,
    width=50,
    font=("Arial", 20),
    fg="#39ff14",
    justify=CENTER
)
label.pack(pady=20)

root.mainloop()
