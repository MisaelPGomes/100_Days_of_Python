from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=300)
window.config(padx= 50, pady=50)


#Entry
input = Entry(width=10)
input.insert(END,string="0")
input.grid(column=1, row=0)


#Labels

label_01 = Label(text="Miles", font=("Arial", 24))
label_01.grid(column=2, row=0)
label_01.config(padx=10)

label_02 = Label(text= "is equal to", font=("Arial", 24))
label_02.grid(column=0, row =1)
label_02.config(padx=10)

label_03 = Label(text="Km", font=("Arial", 24))
label_03.grid(column=2, row=1)
label_01.config(padx=10)

label_04 = Label(text="0", font=("Arial", 24))
label_04.grid(column=1, row=1)

# Button


def miles_to_km():
    miles = float(input.get())
    km = miles*1.609
    label_04.config(text=km)


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)













window.mainloop()