import tkinter as tk

master = tk.Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = tk.Message(master, text=whatever_you_do)
msg.config(bg='light green', font=('times', 24, 'italic'))
msg.pack()

tk.mainloop()
