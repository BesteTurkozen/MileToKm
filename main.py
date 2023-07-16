from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=400, height=200)
window.config(padx=200, pady=100)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=3)

input = Entry(width=10)
print(input.get())
input.grid(column=1, row=2)

def Calculate():
    value = float(input.get())
    if radio_state.get() == 1:
        km_result = value * 0.621371192
        kilometer_result_label.config(text=km_result)
    else:
        mile_result = value * 1.609344
        kilometer_result_label.config(text=mile_result)

calculate_button = Button(text="Calculate", command=Calculate)
calculate_button.grid(column=1, row=4)

def radio_used():
    print(radio_state.get())

radio_state = IntVar()
km_to_mile = Radiobutton(text="Km to Mile", value=1, variable=radio_state)
mile_to_km = Radiobutton(text="Mile to Km", value=2, variable=radio_state)
km_to_mile.grid(column=1, row=0)
mile_to_km.grid(column=1, row=1)

window.mainloop()
