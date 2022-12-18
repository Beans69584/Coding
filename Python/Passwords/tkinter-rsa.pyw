import random
from tkinter import *
from tkinter import ttk
import os 
import time 
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import simpledialog
from tkinter import colorchooser
from tkinter import font
from tkinter import Menu
from tkinter import Spinbox
show_progress_bar = "True"
win = Tk()
win.iconbitmap("icon.ico")
win.title("RSA Encryption and Decryption")
win.resizable(False, False)
monty = ttk.LabelFrame(win, text=' RSA Encryption and Decryption ', name="labelFrame")
monty.grid(column=0, row=0, padx=8, pady=4)
hello = ttk.Label(monty, text="Enter a password:", name="hello").grid(column=0, row=2, sticky='W')
password = scrolledtext.ScrolledText(monty, width=200, height=50, wrap=WORD)
password.grid(column=0, row=3, sticky='W')
password.config(font=("Arial", 10))
button_thing = Label(monty, text="Choose a bit option (above 4096 not recommended. Above 16384 will take a long time): ").grid(column=0, row=4, sticky='W')
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly', name="numberChosen")
numberChosen['values'] = (1024, 2048, 4096, 8192, 16384, 32768, 65536)
numberChosen.grid(column=0, row=5, sticky='W')
numberChosen.current(0)
def encrypt():
    filename = "key.txt"
    filename_key = "key.pem"
    # check box is not empty
    if password.get("1.0", "end-1c") == "":
        messagebox.showerror("Error", "Please enter a password")
        return
    status.configure(text="Encrypting the message...")
    progress_bar['value'] = random.randint(5, 20)
    win.update_idletasks()
    os.system("ruby rsa-password.rb " + " " + password.get("1.0", "end-1c") + " " + filename + " " + number.get())
    time.sleep(1)
    progress_bar['value'] = random.randint(20, 40)
    win.update_idletasks()
    time.sleep(1)
    progress_bar['value'] = random.randint(40, 60)
    win.update_idletasks()
    time.sleep(1)
    progress_bar['value'] = random.randint(60, 80)
    win.update_idletasks()
    time.sleep(1)
    progress_bar['value'] = 100
    with open(filename, 'r') as f:
        data = f.read()
        data = data.replace("\n", "")
        password.delete("1.0", "end-1c")
        password.insert(INSERT, data)
    win.update_idletasks()
    status.configure(text="RSA Encryption and Decryption")


def decrypt():
    # ask for the key with a dialog box
    status.configure(text="Decrypting the message...")
    # ask user to choose a file to decrypt
    filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    filename = filename.replace("/", "\\")
    filename = '"' + filename + '"'
    print(filename)
    # move file to the current directory and rename it to key.txt
    if os.name == "nt":
        os.system("move " + filename + " key.txt")
    else:
        os.system("mv " + filename + " key.txt")
    # ask user to choose a key to decrypt
    filename_key = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Text files", "*.pem"), ("all files", "*.*")))
    filename_key = filename_key.replace("/", "\\")
    filename_key = '"' + filename_key + '"'
    print(filename_key)
    if os.name == "nt":
        os.system("move " + filename_key + " key.pem")
    else:
        os.system("mv " + filename_key + " key.pem")
    # check the files exist and if they do, decrypt the file
    if os.path.isfile("key.txt") and os.path.isfile("key.pem"):
        filename = "key.txt"
        filename_key = "key.pem"
        decrypted = os.popen("ruby rsa-decrypt.rb " + " " + filename + " " + filename_key).read()
        # if there is an error with the ruby script, show the error
        if "error" in decrypted:
            messagebox.showerror("Error", decrypted)
            return
        progress_bar['value'] = random.randint(5, 20)
        win.update_idletasks()
        time.sleep(1)
        progress_bar['value'] = random.randint(20, 40)
        win.update_idletasks()
        time.sleep(1)
        progress_bar['value'] = random.randint(40, 60)
        win.update_idletasks()
        time.sleep(1)
        progress_bar['value'] = random.randint(60, 80)
        win.update_idletasks()
        time.sleep(1)
        progress_bar['value'] = 100
        win.update_idletasks()
        password.delete("1.0", "end-1c")
        password.insert(INSERT, decrypted)

def copy():
    win.clipboard_clear()
    thing = password.get("1.0", "end-1c")
    thing = thing.replace("\n", "")
    win.clipboard_append(thing)



def save():
    filename = filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    with open(filename, 'w') as f:
        f.write(password.get("1.0", "end-1c"))



def clear():
    password.delete("1.0", "end-1c")
    progress_bar['value'] = 0
    win.update_idletasks()
    status.configure(text="RSA Encryption and Decryption")



def _quit():
    win.quit()
    win.destroy()
    exit()



menu_bar = Menu(win)
win.config(menu=menu_bar)


file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)


help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)


toolbar = Menu(win)
win.config(menu=toolbar)
encrypt_button = toolbar.add_command(label="Encrypt", command=encrypt)
decrypt_button = toolbar.add_command(label="Decrypt", command=decrypt)
copy_button = toolbar.add_command(label="Copy", command=copy)
save_button = toolbar.add_command(label="Save", command=save)
clear_button = toolbar.add_command(label="Clear", command=clear)
exit_button = toolbar.add_command(label="Exit", command=_quit)


status = ttk.Label(win, text="RSA Encryption and Decryption", relief=SUNKEN, anchor=W, font='Arial 10 bold')
status.grid(column=0, row=7, sticky='WE')





if show_progress_bar == "True":
    progress_bar = ttk.Progressbar(win, orient=HORIZONTAL, length=1441, mode='determinate')
    progress_bar.grid(column=0, row=8, sticky='W')
else:
    pass



win.mainloop()