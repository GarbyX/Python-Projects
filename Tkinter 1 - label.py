import tkinter as tk

root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter!")
w.pack()

root.mainloop()

# A Label is a Tkinter Widget class, which is used to display text or an image.\n
# The label is a widget that the user just views but not interact with.

myInstruction = input("Press Enter key to exit: ")
print(myInstruction)