from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('SunFamily')

ws['bg']='#5d8a82'

f = ("Times bold", 14)

def nextPage():
    ws.destroy()
    import step2

Label(
    ws,
    text="Ml Algorithms Software",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)


Button(
    ws, 
    text="Continue", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
