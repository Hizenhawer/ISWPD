from tkinter import *
from tkinter import ttk
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
    print(sv.get())

def format_data(elevation, descent, length, color):
    return [float(elevation)/1000, float(descent)/1000, float(length)/10, color/4]
def function_callback(thereTime, returnTime, there_model, return_model, elevation, descent, length, color):
    predicted_there_time = there_model.predict([format_data(elevation, descent, length, color)])[0]
    predicted_return_time = return_model.predict([format_data(elevation, descent, length, color)])[0]
    thereTime.set(predicted_there_time)
    returnTime.set(predicted_return_time)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    there_model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes = (5, 2), random_state = 1)
    X = list(DatabaseHandler.training_data)
    Y_there = list(DatabaseHandler.training_results_there)
    there_model.fit(X, Y_there)
    return_model = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)
    Y_return = list(DatabaseHandler.training_results_return)
    return_model.fit(X, Y_return)


    root = Tk()
    root.title('Przwidywanie czasu przejścia danego szlaku')
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    inclineCallback = DoubleVar()
    descentCallback = DoubleVar()
    lengthCallback = DoubleVar()
    selectedColor = StringVar()
    ENTRY_INCLINE = Entry(frm, textvariable=inclineCallback)
    ENTRY_DESCENT = Entry(frm, textvariable=descentCallback)
    ENTRY_LENGTH = Entry(frm, textvariable=lengthCallback)
    ENTRY_INCLINE.grid(column=2, row=2)
    ENTRY_DESCENT.grid(column=3, row=2)
    ENTRY_LENGTH.grid(column=4, row=2)
    ttk.Label(frm, text="Kolor", padding=10).grid(column=1, row=1)
    ttk.Label(frm, text="Wzniesienie", padding=10).grid(column=2, row=1)
    ttk.Label(frm, text="Zejście", padding=10).grid(column=3, row=1)
    ttk.Label(frm, text="Długość (km)", padding=10).grid(column=4, row=1)
    colors = ['CZERWONY', "NIEBIESKI", "CZARNY", "ZIELONY"]
    cb = ttk.Combobox(frm, textvariable=selectedColor, values=colors, state='readonly')
    cb.grid(column=1,row=2)
    cb.current(0)
    ttk.Label(frm, text="Przewidywany czas przejścia\ntam (min):", padding=10).grid(column=1, row=3)
    ttk.Label(frm, text="Przewidywany czas przejścia\nz powrotem (min):", padding=10).grid(column=2, row=3)
    thereTime = DoubleVar()
    returnTime = DoubleVar()
    there_result = Entry(frm, textvariable=thereTime)
    return_result = Entry(frm, textvariable=returnTime)
    there_result.grid(column=1, row=4)
    return_result.grid(column=2, row=4)
    there_result['state'] = 'readonly'
    return_result['state'] = 'readonly'
    ttk.Button(frm, text="Przewidź czas przejścia", command=lambda: function_callback(thereTime, returnTime, there_model, return_model, ENTRY_INCLINE.get(), ENTRY_DESCENT.get(), ENTRY_LENGTH.get(), colors.index(cb.get())+1)).grid(column=3,row=4)
    ttk.Button(frm, text="Wyjdź", command=root.destroy).grid(column=4, row=4)
    root.mainloop()
