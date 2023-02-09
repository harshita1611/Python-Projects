from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300 , height=100)
window.config(padx=30,pady=30)

miles_input = Entry(width=10)
miles_input.grid(column=1 , row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2 , row=0)


is_equal_to_lable =Label(text="is equal to")
is_equal_to_lable.grid(column=0 , row=1)

kilometer_result_label =Label(text="0")
kilometer_result_label.grid(column=1 , row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(column= 2, row=1)

def calculate_km():
    miles=float(miles_input.get())
    kilometers = 1.6094 * miles
    kilometer_result_label.config(text=f"{kilometers}")

calculate_button= Button(text="Calculate",command=calculate_km)
calculate_button.grid(column=1, row=2)


window.mainloop()