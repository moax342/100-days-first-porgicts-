import tkinter

window = tkinter.Tk()
window.title("Klm to Mile Converter")
window.config(padx=20,pady=20)

def calculate_miles():
    new_text=int(value_input.get())*1.609
    value_label.config(text=round(new_text,2))


# equal_label
equal_label = tkinter.Label(text="Is Equal To:")
equal_label.grid(column=0, row=1)

# value_label
value_label = tkinter.Label(text=" 0 ")
value_label.grid(column=1,row=1)

# miles_label
miles_label = tkinter.Label(text=" Miles ")
miles_label.grid(column=2,row=0)

# klm_label
klm_label = tkinter.Label(text=" KLM ")
klm_label.grid(column=2,row=1)

# calculate_button
calculate_button = tkinter.Button(text="Calculate", command=calculate_miles)
calculate_button.grid(column=1,row=2)

# value_input
value_input =tkinter.Entry(width=10)
value_input.grid(column=1,row=0)

window.mainloop()
