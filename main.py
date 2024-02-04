from tkinter import *
from tkinter import messagebox
import pyperclip
import json
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for c in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for ch in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():

    web = entry_web.get().capitalize()

    try:
        with open('data.json', 'r') as arch_data:

            data = json.load(arch_data)

    except FileNotFoundError:
        messagebox.showerror(title='Error', message="No Data File Found")

    else:

        new_data = data.get(web)

        try:
            messagebox.showinfo(title='Info', message=f"Email:{new_data['email']}\nPassword:{new_data['password']}")

        except TypeError:
            messagebox.showerror(title='Error', message="No Website Found")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def create_file(nw_dt):

    try:
        with open('data.json', 'w') as arch_data:

            json.dump(nw_dt, arch_data, indent=4)

    except IOError as msj:
        print(msj)


def save():

    web = entry_web.get().capitalize()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        web: {
            'email': email,
            'password': password,
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title='Error', message="Please don't leave any fields empty!")
    else:

        try:
            with open('data.json', 'r') as data_file:

                data = json.load(data_file)
                data.update(new_data)

        except(IOError, FileNotFoundError):
            create_file(new_data)

        else:

            data.update(new_data)

            try:
                with open('data.json', 'w') as arch_data:

                    json.dump(data, arch_data, indent=4)

            except IOError as msj:
                print(msj)

        finally:

            entry_web.delete(first=0, last=END)
            entry_email.delete(first=0, last=END)
            entry_password.delete(first=0, last=END)
            entry_web.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

"""CANVAS"""
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)  # Los primeros valores son la posicion 'x' e 'y'
canvas.grid(row=0, column=1)

"""LABEL"""
website_label = Label(text='Website:', font=('Arial', 10))
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:', font=('Arial', 10))
email_label.grid(row=2, column=0)
password_label = Label(text='Password:', font=('Arial', 10))
password_label.grid(row=3, column=0)

"""ENTRY"""
entry_web = Entry(width=35)
entry_web.grid(row=1, column=1, columnspan=2)
entry_web.focus()
entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, 'roberto90@gmail.com')
entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

"""BUTTON"""
generate_pass_button = Button(text='Generate Password', command=password_generator)
generate_pass_button.grid(row=3, column=3)
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(row=1, column=3)

window.mainloop()

