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

tab_control =  ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='AIM')
tab_control.add(tab2, text='ESP')

lb1 = Label(tab1, text='AIM')
lb1.grid(column=0, row=0)

lb2 = Label(tab2, text='ESP')
lb2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

window.mainloop()

