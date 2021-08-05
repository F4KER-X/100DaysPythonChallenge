import tkinter
from tkinter.constants import END
from tkinter import messagebox
import random
import pyperclip
# ------------------------- PASSWORD GENERATOR ---------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters)
                        for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols)
                        for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers)
                        for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    if len(pass_entry.get()) != 0:
        pass_entry.delete(0, END)
        pass_entry.insert(0, password)
        pyperclip.copy(password)
    else:
        pass_entry.insert(0, password)
        pyperclip.copy(password)

# ------------------------- SAVE PASSWORD ---------------------------- #


def save():
    if len(web_entry.get()) == 0 or len(pass_entry.get()) == 0 or \
            len(email_entry.get()) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web_entry.get(
        ), message=f"There are the details entered: \nEmail: {email_entry.get()} \
            \nPassword: {pass_entry.get()} \nIs it ok to save?")
        if is_ok:
            with open(r"Day 029 - Password Manager/data.txt", mode="a") as \
                    file:
                file.write(
                    f"{web_entry.get()} | {email_entry.get()} | {pass_entry.get()}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

image_location = r"Day 029 - Password Manager\logo.png"
canvas = tkinter.Canvas(width=200, height=200)
lock_image = tkinter.PhotoImage(file=image_location)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

label_1 = tkinter.Label(text="Website:")
label_1.grid(column=0, row=1)

label_2 = tkinter.Label(text="Email/Username:", padx=20)
label_2.grid(column=0, row=2)

label_3 = tkinter.Label(text="Password:")
label_3.grid(column=0, row=3)

web_entry = tkinter.Entry(width=35)
web_entry.grid(column=1, row=1, sticky="ew", columnspan=2)
web_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, sticky="ew", columnspan=2)
email_entry.insert(0, "example@example.com")

pass_entry = tkinter.Entry(width=21)
pass_entry.grid(column=1, row=3, sticky="ew")

gen_button = tkinter.Button(text="Generate Password", command=generate)
gen_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
