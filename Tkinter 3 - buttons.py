import tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()

frame = tk.Frame(root)
frame.pack()
slogan = tk.Button(frame, text="Hello", command=write_slogan)
slogan.pack(side=tk.LEFT)
button = tk.Button(frame, text="QUIT", fg="red", command=quit)
button.pack(side=tk.LEFT)


root.mainloop()
