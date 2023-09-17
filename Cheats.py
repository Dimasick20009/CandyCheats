from tkinter import *
from tkinter import ttk

root = Tk()
root.title('CandyCheats')
root.geometry('400x250')
root.resizable(width=False, height=False)
root.iconbitmap("icon.ico")
root.image = PhotoImage(file='logo.png')
bg_logo = Label(root, image=root.image)
bg_logo.grid(row=0,column=0)

tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='ESP')
tab_control.add(tab2, text='AIM')

lb1 = Label(tab1, text='ESP')
lb1.grid(column=0, row=0)

lb2 = Label(tab1, text='ESP')
lb2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')
root.mainloop()


