
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generate():

    password_entry.delete(0, END)

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)




# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():

    new_website = website_entry.get()
    new_email_name = email_entry.get()
    new_password = password_entry.get()

    if len(new_website) == 0 or len(new_email_name) == 0 or len(new_password) == 0 :
        messagebox.showinfo(title= "oop", message="Don't leave blank fields")
    else:

        is_ok = messagebox.askokcancel(title= new_website, message=f"These are the details entered: \nEmail: {new_email_name} "
                               f"\nPassword: {new_password} \nIs it ok to save?")

        if is_ok:
            with open('data.txt', "a") as file:
                file.write(f" {new_website} | {new_email_name} | {new_password} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


 # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)


email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,"blablabla@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


#Buttons
generate_password_button = Button(text="Generate Password", command=password_generate)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
