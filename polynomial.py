import tkinter

window = tkinter.Tk()
window.configure(bg="blue")
widget = tkinter
def home():
    window.destroy()
    import page1
def try_next():
    window.destroy()
    import step3
def add_function(): 
    i=int(textbox1.get())
    
    d=int(textbox2.get())
    m=int(textbox3.get())
    import pandas as pd
    import numpy as np 
    import matplotlib.pyplot as plt
    import seaborn as sns
    from tkinter.filedialog import askopenfilename
    filename=askopenfilename()
    data=pd.read_csv(filename)
    x=data.iloc[:,[i]].values
    y=data.iloc[:,[d]].values
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
    
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures
    poly=PolynomialFeatures(degree=5)
    x_train=poly.fit_transform(x_train)
    x_test=poly.fit_transform(x_test)
    reg=LinearRegression()
    reg.fit(x_train,y_train)
    #polynomial prediction
    y_pred=reg.predict(x_test)
    pred=reg.predict(poly.fit_transform([[m]]))
    from sklearn.metrics import r2_score
    accuracy=r2_score(y_test,y_pred)

   
    Label1.configure(text="Predicted value:"+str(pred),fg="white",bg="coral")
    Label2.configure(text="Accuracy:"+str(accuracy),fg="white",bg="coral")
    
    
textbox1 = widget.Entry()
textbox1.pack()
textbox1.place(x=365,y=25,height=25,width=150)

textbox2 =widget.Entry()
textbox2.pack()
textbox2.place(x=365,y=60,height=25,width=150)


textbox3 =widget.Entry()
textbox3.pack()
textbox3.place(x=365,y=100,height=25,width=150)

button1 =widget.Button()
button1.pack()
button1.place(x=325,y=140,height=30,width=190)
button1.configure(text="Conform your csv file",fg='green')
button1.configure(command=add_function)

Label1=widget.Label()
Label1.pack()
Label1.configure(bg="blue")
Label1.place(x=325,y=250,height=30,width=260)


Label2=widget.Label()
Label2.pack()
Label2.configure(bg="blue")
Label2.place(x=325,y=290,height=30,width=280)

Label3=widget.Label()
Label3.pack()
Label3.configure(text="independent value:",bg='blue',font='bold')
Label3.place(x=205,y=26,height=30,width=140)

Label4=widget.Label()
Label4.pack()
Label4.configure(text="dependent value:",bg='blue',font='bold')
Label4.place(x=205,y=60,height=30,width=140)

Label5=widget.Label()
Label5.pack()
Label5.configure(text="prediction value:",bg='blue',font='bold')
Label5.place(x=205,y=100,height=30,width=140,)

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


