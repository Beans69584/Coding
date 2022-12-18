import random
from tkinter import *
from tkinter import ttk
import os 
import time 
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import Menu
global languageChoice
global show_progress_bar
global win
global monty
global hello_label
global password
global button_thing
global number
global numberChosen
global status
global progress_bar
global encrypt_button
global decrypt_button
global exit_button
global font_choice
global win2
font_choice = "Arial"
# check if being run in the correct directory
if os.path.isfile("tkinter-rsa.pyw") == False:
    messagebox.showerror("Error", "Please run this program in the correct directory")
    exit()
if os.system("ruby -v") != 0:
    messagebox.showerror("Error", "Ruby is not installed. Please install Ruby to use this program.")
    exit()
cwd = os.getcwd()
if os.path.isfile(cwd + "\\rsa-password.rb") == False:
    messagebox.showerror("Error", "rsa-password.rb is not installed. Please install rsa-password.rb to use this program.")
    exit()
if os.path.isfile(cwd + "\\rsa-decrypt.rb") == False:
    messagebox.showerror("Error", "rsa-decrypt.rb is not installed. Please install rsa-decrypt.rb to use this program.")
    exit()
show_progress_bar = "True"
win = Tk()
win.title("RSA Encryption and Decryption")
win.resizable(False, False)
monty = ttk.LabelFrame(win, text=' RSA Encryption and Decryption ', name="labelFrame")
monty.grid(column=0, row=0, padx=8, pady=4)
hello_label = ttk.Label(monty, text="Enter a password:", name="hello_label").grid(column=0, row=2, sticky='W')
password = scrolledtext.ScrolledText(monty, width=200, height=50, wrap=WORD)
password.grid(column=0, row=3, sticky='W')
password.config(font=(font_choice, 10))
button_thing = Label(monty, text="Choose a bit option (above 4096 not recommended. Above 16384 will take a long time): ").grid(column=0, row=4, sticky='W')
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number, state='readonly', name="numberChosen")
numberChosen['values'] = (1024, 2048, 4096, 8192, 16384, 32768, 65536)
numberChosen.grid(column=0, row=5, sticky='W')
numberChosen.current(0)
# print hello_label 
def encrypt():
    filename = "key.txt"
    filename_key = "key.pem"
    if password.get("2.0", "end-1c") != "":
        messagebox.showerror("Error", "Please enter only one line")
        return
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
    status.configure(text="Decrypting the message...")
    filename = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    filename = filename.replace("/", "\\")
    filename = '"' + filename + '"'
    print(filename)
    if os.name == "nt":
        os.system("move " + filename + " key.txt")
    else:
        os.system("mv " + filename + " key.txt")
    filename_key = filedialog.askopenfilename(initialdir="./", title="Select file", filetypes=(("Text files", "*.pem"), ("all files", "*.*")))
    filename_key = filename_key.replace("/", "\\")
    filename_key = '"' + filename_key + '"'
    print(filename_key)
    if os.name == "nt":
        os.system("move " + filename_key + " key.pem")
    else:
        os.system("mv " + filename_key + " key.pem")
    if os.path.isfile("key.txt") and os.path.isfile("key.pem"):
        filename = "key.txt"
        filename_key = "key.pem"
        decrypted = os.popen("ruby rsa-decrypt.rb " + " " + filename + " " + filename_key).read()
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
    filename = filedialog.asksaveasfilename(initialdir="./", title="Select file", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
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
def settings():
    global win2
    win2 = Toplevel()
    win2.title("Settings")
    win2.resizable(False, False)
    thing = ttk.Combobox(win2, values=["English", "Spanish", "French", "German", "Italian"], state="readonly")
    thing.grid(column=0, row=0)
    thing.current(0)
    blank_space = ttk.Label(win2, text=" ").grid(column=0, row=1)
    save_button = ttk.Button(win2, text="Save", command=lambda: save_settings(thing.get()))
    save_button.grid(column=0, row=4)
    win2.mainloop()
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
settings_button = toolbar.add_command(label="Settings", command=settings)
status = ttk.Label(win, text="RSA Encryption and Decryption", relief=SUNKEN, anchor=W, font='Arial 10 bold')
status.grid(column=0, row=7, sticky='WE')
if show_progress_bar == "True":
    progress_bar = ttk.Progressbar(win, orient=HORIZONTAL, length=1441, mode='determinate')
    progress_bar.grid(column=0, row=8, sticky='W')
else:
    pass
def save_settings(languageChoice):
    print(languageChoice)
    if languageChoice == "English":
        with open ("settings.txt", "w") as f:
            f.write("English")
        win.title("RSA Encryption and Decryption")
        # remove all commands from toolbar
        monty.configure(text="RSA Encryption and Decryption")
        toolbar.delete(0, "end")
        # add new widgets to toolbar
        encrypt_button = toolbar.add_command(label="Encrypt", command=encrypt)
        decrypt_button = toolbar.add_command(label="Decrypt", command=decrypt)
        copy_button = toolbar.add_command(label="Copy", command=copy)
        save_button = toolbar.add_command(label="Save", command=save)
        clear_button = toolbar.add_command(label="Clear", command=clear)
        exit_button = toolbar.add_command(label="Exit", command=_quit)
        settings_button = toolbar.add_command(label="Settings", command=settings)
        hello_label = ttk.Label(monty, text="Enter a password:", name="hello_label").grid(column=0, row=2, sticky='W')
        button_thing = Label(monty, text="Choose a bit option (above 4096 not recommended. Above 16384 will take a long time):                                                     ").grid(column=0, row=4, sticky='W')
        status.configure(text="RSA Encryption and Decryption")
        win.update_idletasks()
    elif languageChoice == "Spanish":
        with open ("settings.txt", "w") as f:
            f.write("Spanish")
        win.title("Encriptación y desencriptación RSA")
        # remove all commands from toolbar
        monty.configure(text="Encriptación y desencriptación RSA")
        toolbar.delete(0, "end")
        # add new widgets to toolbar
        encrypt_button = toolbar.add_command(label="Encriptar", command=encrypt)
        decrypt_button = toolbar.add_command(label="Desencriptar", command=decrypt)
        copy_button = toolbar.add_command(label="Copiar", command=copy)
        save_button = toolbar.add_command(label="Guardar", command=save)
        clear_button = toolbar.add_command(label="Limpiar", command=clear)
        exit_button = toolbar.add_command(label="Salir", command=_quit)
        settings_button = toolbar.add_command(label="Ajustes", command=settings)
        hello_label = ttk.Label(monty, text="Introduzca una contraseña:", name="hello_label").grid(column=0, row=2, sticky='W')
        button_thing = Label(monty, text="Elija una opción de bits (por encima de 4096 no se recomienda. Por encima de 16384 tardará mucho tiempo):                                                      ").grid(column=0, row=4, sticky='W')
        status.configure(text="Encriptación y desencriptación RSA")
        win.update_idletasks()
    elif languageChoice == "French":
        with open ("settings.txt", "w") as f:
            f.write("French")
        win.title("Chiffrement et déchiffrement RSA")
        # remove all commands from toolbar
        monty.configure(text="Chiffrement et déchiffrement RSA")
        toolbar.delete(0, "end")
        # add new widgets to toolbar
        encrypt_button = toolbar.add_command(label="Chiffrer", command=encrypt)
        decrypt_button = toolbar.add_command(label="Déchiffrer", command=decrypt)
        copy_button = toolbar.add_command(label="Copier", command=copy)
        save_button = toolbar.add_command(label="Enregistrer", command=save)
        clear_button = toolbar.add_command(label="Effacer", command=clear)
        exit_button = toolbar.add_command(label="Quitter", command=_quit)
        settings_button = toolbar.add_command(label="Paramètres", command=settings)
        hello_label = ttk.Label(monty, text="Entrez un mot de passe:", name="hello_label").grid(column=0, row=2, sticky='W')
        button_thing = Label(monty, text="Choisissez une option de bits (au-dessus de 4096 non recommandé. Au-dessus de 16384 prendra beaucoup de temps):  ").grid(column=0, row=4, sticky='W')
        status.configure(text="Chiffrement et déchiffrement RSA")
        win.update_idletasks()
    elif languageChoice == "German":
        with open ("settings.txt", "w") as f:
            f.write("German")
        win.title("RSA-Verschlüsselung und -Entschlüsselung")
        # remove all commands from toolbar
        monty.configure(text="RSA-Verschlüsselung und -Entschlüsselung")
        toolbar.delete(0, "end")
        # add new widgets to toolbar
        encrypt_button = toolbar.add_command(label="Verschlüsseln", command=encrypt)
        decrypt_button = toolbar.add_command(label="Entschlüsseln", command=decrypt)
        copy_button = toolbar.add_command(label="Kopieren", command=copy)
        save_button = toolbar.add_command(label="Speichern", command=save)
        clear_button = toolbar.add_command(label="Löschen", command=clear)
        exit_button = toolbar.add_command(label="Beenden", command=_quit)
        settings_button = toolbar.add_command(label="Einstellungen", command=settings)
        hello_label = ttk.Label(monty, text="Geben Sie ein Passwort ein:", name="hello_label").grid(column=0, row=2, sticky='W')
        button_thing = Label(monty, text="Wählen Sie eine Bit-Option (über 4096 nicht empfohlen. Über 16384 wird viel Zeit benötigen):                                                        ").grid(column=0, row=4, sticky='W')
        status.configure(text="RSA-Verschlüsselung und -Entschlüsselung")
        win.update_idletasks()
    elif languageChoice == "Italian":
        with open ("settings.txt", "w") as f:
            f.write("Italian")
        win.title("Crittografia e decrittografia RSA")
        # remove all commands from toolbar
        monty.configure(text="Crittografia e decrittografia RSA")
        toolbar.delete(0, "end")
        # add new widgets to toolbar
        encrypt_button = toolbar.add_command(label="Criptare", command=encrypt)
        decrypt_button = toolbar.add_command(label="Decriptare", command=decrypt)
        copy_button = toolbar.add_command(label="Copiare", command=copy)
        save_button = toolbar.add_command(label="Salvare", command=save)
        clear_button = toolbar.add_command(label="Cancellare", command=clear)
        exit_button = toolbar.add_command(label="Uscire", command=_quit)
        settings_button = toolbar.add_command(label="Impostazioni", command=settings)
        hello_label = ttk.Label(monty, text="Inserisci una password:", name="hello_label").grid(column=0, row=2, sticky='W')
        button_thing = Label(monty, text="Scegliere un'opzione di bit (oltre 4096 non raccomandato. Oltre 16384 richiederà molto tempo):                                                       ").grid(column=0, row=4, sticky='W')
        status.configure(text="Crittografia e decrittografia RSA")
        win.update_idletasks()
    else:
        with open ("settings.txt", "w") as f:
            f.write("English")
        win.title("RSA Encryption and Decryption")
        # remove all commands from toolbar
        monty.configure(text="RSA Encryption and Decryption")
        toolbar.delete(0, "end")
        # add new widgets to toolbar
        encrypt_button = toolbar.add_command(label="Encrypt", command=encrypt)
        decrypt_button = toolbar.add_command(label="Decrypt", command=decrypt)
        copy_button = toolbar.add_command(label="Copy", command=copy)
        save_button = toolbar.add_command(label="Save", command=save)
        clear_button = toolbar.add_command(label="Clear", command=clear)
        exit_button = toolbar.add_command(label="Exit", command=_quit)
        settings_button = toolbar.add_command(label="Settings", command=settings)
        hello_label = ttk.Label(monty, text="Enter a password:", name="hello_label").grid(column=0, row=2, sticky='W')
        button_thing = Label(monty, text="Choose a bit option (above 4096 not recommended. Above 16384 will take a long time):                                             ").grid(column=0, row=4, sticky='W')
        status.configure(text="RSA Encryption and Decryption")
        win.update_idletasks()
if os.path.isfile("settings.txt") == True:
    # get first line of settings.txt
    # open as read-write
    with open ("settings.txt", "r+") as f:
        first_line = f.readline()
        # check if there is anything in the first line
        if first_line != "":
            # check if the first line is a valid language
            if first_line == "English" or first_line == "French" or first_line == "Spanish" or first_line == "German" or first_line == "Italian" or first_line == "Portuguese" or first_line == "Russian" or first_line == "Japanese" or first_line == "Chinese" or first_line == "Korean":
                languageChoice = first_line
                save_settings(languageChoice)
            else:
                f.write("English")
                languageChoice = "English"
                save_settings(languageChoice)
        else:
            f.write("English")
            languageChoice = "English"
            save_settings(languageChoice)
win.mainloop()