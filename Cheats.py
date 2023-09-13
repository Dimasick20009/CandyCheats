from tkinter import *
from tkinter import ttk

window = Tk()
window.title("CandyCheats")

width = 400
height = 300
x = 200
y = 300
window.geometry(f"{width}x{height}+{x}+{y}")
window.resizable(False,False)
window.iconbitmap("icon.ico")
window.image = PhotoImage(file='logo.png')
bg_logo = Label(window, image=window.image)
bg_logo.grid(row=0,column=0)

window.mainloop()

