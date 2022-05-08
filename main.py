# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from array import array
from tkinter import *
from tkinter import ttk

import numpy
from sklearn.neural_network import MLPClassifier
import DatabaseHandler

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def callback_name(sv):
    print(sv.get())


def callback_color(sv):
    print(sv.get())


def callback_incline(sv):
    print(sv.get())


def callback_descent(sv):
    print(sv.get())


def callback_length(sv):
    print(sv.get())


def callback_time(sv):
    print(sv.get())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    X = (list(map(lambda x: [x.elevation, x.descent, x.length], DatabaseHandler.data)))
    Y = (list(map(lambda x: abs(x.time[0] - x.time[1]), DatabaseHandler.data)))

    for o in DatabaseHandler.training_data:
            print(o)
    for o in DatabaseHandler.training_results:
            print(o)

    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes = (5, 2), random_state = 1)
    # clf.fit(X,Y)
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    nameCallback = StringVar()
    colorCallback = StringVar()
    inclineCallback = DoubleVar()
    descentCallback = DoubleVar()
    lengthCallback = DoubleVar()
    timeCallback = DoubleVar()
    nameCallback.trace("w", lambda name, index, mode, sv=nameCallback: callback_name(sv))
    colorCallback.trace("w", lambda name, index, mode, sv=colorCallback: callback_color(sv))
    inclineCallback.trace("w", lambda name, index, mode, sv=inclineCallback: callback_incline(sv))
    descentCallback.trace("w", lambda name, index, mode, sv=descentCallback: callback_descent(sv))
    lengthCallback.trace("w", lambda name, index, mode, sv=lengthCallback: callback_length(sv))
    timeCallback.trace("w", lambda name, index, mode, sv=timeCallback: callback_time(sv))
    ENTRY_NAME = Entry(frm, textvariable=nameCallback)
    ENTRY_COLOR = Entry(frm, textvariable=colorCallback)
    ENTRY_INCLINE = Entry(frm, textvariable=inclineCallback)
    ENTRY_DESCENT = Entry(frm, textvariable=descentCallback)
    ENTRY_LENGTH = Entry(frm, textvariable=lengthCallback)
    ENTRY_TIME = Entry(frm, textvariable=timeCallback)
    ttk.Label(frm, text="Wyszukaj szlaki górskie").grid(column=0, row=0)
    ttk.Label(frm, text="Nazwa", padding=10).grid(column=0, row=1)
    ttk.Label(frm, text="Kolor", padding=10).grid(column=1, row=1)
    ttk.Label(frm, text="Wzniesienie", padding=10).grid(column=2, row=1)
    ttk.Label(frm, text="Zejście", padding=10).grid(column=3, row=1)
    ttk.Label(frm, text="Długość (km)", padding=10).grid(column=4, row=1)
    ttk.Label(frm, text="Czas przejścia (min)", padding=10).grid(column=5, row=1)
    ENTRY_NAME.grid(column=0, row=2)
    ENTRY_COLOR.grid(column=1, row=2)
    ENTRY_INCLINE.grid(column=2, row=2)
    ENTRY_DESCENT.grid(column=3, row=2)
    ENTRY_LENGTH.grid(column=4, row=2)
    ENTRY_TIME.grid(column=5, row=2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=5, row=0)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
