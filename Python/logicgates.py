import tkinter as tk
from tkinter import ttk


def logicGate():
    if gate.get() == "AND":
        if input1.get() == "1" and input2.get() == "1":
            output.set("1")
        else:
            output.set("0")
    elif gate.get() == "OR":
        if input1.get() == "1" or input2.get() == "1":
            output.set("1")
        else:
            output.set("0")
    elif gate.get() == "XOR":
        if input1.get() == "1" and input2.get() == "0" or input1.get() == "0" and input2.get() == "1":
            output.set("1")
        else:
            output.set("0")
    elif gate.get() == "NOT":
        if input1.get() == "1":
            output.set("0")
        else:
            output.set("1")
    elif gate.get() == "NAND":
        if input1.get() == "1" and input2.get() == "1":
            output.set("0")
        else:
            output.set("1")
    elif gate.get() == "NOR":
        if input1.get() == "1" or input2.get() == "1":
            output.set("0")
        else:
            output.set("1")
    elif gate.get() == "XNOR":
        if input1.get() == "1" and input2.get() == "0" or input1.get() == "0" and input2.get() == "1":
            output.set("0")
        else:
            output.set("1")
    else:
        output.set("Invalid input")


root = tk.Tk()
root.iconbitmap("favicon.ico")
root.title("Logic Gate Simulator")
root.geometry("525x200")
root.resizable(False, False)

gate = tk.StringVar()
input1 = tk.StringVar()
input2 = tk.StringVar()
output = tk.StringVar()

gateLabel = ttk.Label(
    root, text="Enter the type of logic gate (AND, OR, XOR, NOT, NAND, NOR, XNOR): ")
gateLabel.grid(row=0, column=0, padx=5, pady=5)
gateEntry = ttk.Entry(root, textvariable=gate)
gateEntry.grid(row=0, column=1, padx=5, pady=5)

input1Label = ttk.Label(root, text="Enter the first input: ")
input1Label.grid(row=1, column=0, padx=5, pady=5)
input1Entry = ttk.Entry(root, textvariable=input1)
input1Entry.grid(row=1, column=1, padx=5, pady=5)

input2Label = ttk.Label(root, text="Enter the second input: ")
input2Label.grid(row=2, column=0, padx=5, pady=5)
input2Entry = ttk.Entry(root, textvariable=input2)
input2Entry.grid(row=2, column=1, padx=5, pady=5)

outputLabel = ttk.Label(root, text="Output: ")
outputLabel.grid(row=3, column=0, padx=5, pady=5)
outputEntry = ttk.Entry(root, textvariable=output, state="readonly")
outputEntry.grid(row=3, column=1, padx=5, pady=5)

calculateButton = ttk.Button(root, text="Simulate", command=logicGate)
calculateButton.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()
