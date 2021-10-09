"""import tkinter as tk
from tkinter import*
win = Tk()
def nextPages():
    win.destroy()
    import step3

class App(tk.Frame):
    def __init__(self):
        super().__init__()

        self.pack(fill=tk.BOTH, expand=1)

        self.stringVars = []
        self.entries = []

        for offset in range(2):
            stringVar = tk.StringVar()
            self.stringVars.append(stringVar)

            entry = tk.Entry(self, width=15, background='white',
                             textvariable=stringVar, justify=tk.CENTER, font='-weight bold')
            entry.grid(padx=10, pady=5, row=17 + offset, column=1, sticky='W,E,N,S')
            self.entries.append(entry)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("200x175")
    app = App()
    root.mainloop()
b = Button(win,text = "continue",command=nextPages)  
  
b.pack()

win.mainloop()"""

from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('SunFamily')
ws['bg']='#5d8a82'
L1 = Label(ws, text="User Name")
L1.pack( side = LEFT)
for data in range(4):
    E1 = Entry(ws, bd =2)
    E1.pack(side = RIGHT)


ws.mainloop()


























