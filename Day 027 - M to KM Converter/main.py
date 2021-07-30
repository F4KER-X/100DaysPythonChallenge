import tkinter


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def convert():
    CONSTANT = 1.609
    new_value = float(miles_entry.get()) * CONSTANT
    value_label.config(text=str(round(new_value)))


miles_entry = tkinter.Entry(width=10)
miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(row=1, column=0)

value_label = tkinter.Label(text="0")
value_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", command=convert)
calculate_button.grid(row=2, column=1)

window.mainloop()
