import tkinter

window = tkinter.Tk()
widget = tkinter
window.configure(bg='blue')
def home():
    window.destroy()
    import page1
def try_next():
    window.destroy()
    import step3
def add_function(): 
    i = list(map(int,(textbox1.get()).split()))
    c = textbox2.get()
    cluster =int(textbox3.get())

    import pandas as pd
    import numpy as np
    from tkinter.filedialog import askopenfile
    
    filename=askopenfile()
    data=pd.read_csv(filename)
    
    x=data.iloc[:,i].values
    from sklearn.cluster import AgglomerativeClustering
    hc=AgglomerativeClustering(n_clusters=cluster,linkage='ward')
    y_pred=hc.fit_predict(x)
   
   
    df=data
    
    df['target']=y_pred

    df.to_csv(c)    
   
    
 
   

    
textbox1 = widget.Entry()
textbox1.pack()
textbox1.place(x=367,y=25,height=25,width=150)

textbox2 =widget.Entry()
textbox2.pack()
textbox2.place(x=367,y=60,height=25,width=150)


textbox3 =widget.Entry()
textbox3.pack()
textbox3.place(x=367,y=100,height=25,width=150)

button1 =widget.Button()
button1.pack()
button1.place(x=325,y=140,height=30,width=190)
button1.configure(text="Conform your csv file",fg='green')
button1.configure(command=add_function)

Label1=widget.Label()
Label1.pack()
Label1.configure(bg="blue")
Label1.place(x=325,y=250,height=30,width=260)


Label3=widget.Label()
Label3.pack()
Label3.configure(text="independent value:",bg='blue',font='bold')
Label3.place(x=205,y=26,height=30,width=150)

Label4=widget.Label()
Label4.pack()
Label4.configure(text="file path of target data :",bg='blue',font='bold')
Label4.place(x=185,y=60)

Label5=widget.Label()
Label5.pack()
Label5.configure(text="n_clusters :",bg='blue',font='bold')
Label5.place(x=185,y=100)


button2 =widget.Button()
button2.pack()
button2.place(x=0,y=340,height=30,width=190)
button2.configure(text="back to home",fg='green',bg='lightgreen')
button2.configure(command=home)

button3 =widget.Button()
button3.pack()
button3.place(x=505,y=340,height=30,width=190)
button3.configure(text="Try Another one model",fg='green',bg='lightgreen')
button3.configure(command=try_next)



window.title("SunFamily")
window.geometry("800x400")
window.mainloop()


