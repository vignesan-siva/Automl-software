import tkinter

window = tkinter.Tk()
widget = tkinter

def simple():
    window.destroy()
    import simple_linear
    
def multi():
    window.destroy()
    import multi_linear
def poly():
    window.destroy()
    import polynomial
def SVR():
    window.destroy()
    import SVR
def DTR():
    window.destroy()
    import DecisionTreeRegression
def RFR():
    window.destroy()
    import RandomForestRegressor
def Logi():
    window.destroy()
    import logisticRegression
def Naive():
    window.destroy()
    import naivebayes
def KNN():
    window.destroy()
    import KNN
def SVC():
    window.destroy()
    import SVC
def DTC():
    window.destroy()
    import DecisionTreeClassifier
def RFC():
    window.destroy()
    import RandomForestRegressor
def kmeans():
    window.destroy()
    import kmeans
def hirarchy():
    window.destroy()
    import hirarchy

Label1=widget.Label()
Label1.pack()
Label1.configure(text="SELECT THE ML MODEL",fg='yellow',bg='blue',font='bold')
Label1.place(x=295,y=1,height=30,width=250)  
#regression lavel

regl=widget.Label()
regl.pack()
regl.configure(text="Regression",fg="lightgreen",bg="blue",font='bold')
regl.place(x=80,y=60) 


#simple linearRegression
button1 =widget.Button()
button1.pack()
button1.place(x=75,y=100)
button1.configure(text="1.Simple Linear Regression",bg='darkgoldenrod')
button1.configure(command=simple)
#multilinearRegression
button2 =widget.Button()
button2.pack()
button2.place(x=75,y=130)
button2.configure(text="2.Multi Linear Regression",bg='darkgoldenrod')
button2.configure(command=multi)
#polynomialFeatures
button3 =widget.Button()
button3.pack()
button3.place(x=75,y=160)
button3.configure(text="3.Polynomial Regression",bg='darkgoldenrod')
button3.configure(command=poly)
#svm
button71 =widget.Button()
button71.pack()
button71.place(x=75,y=190)
button71.configure(text="4.Support Vectore Machine",bg='darkgoldenrod')
button71.configure(command=SVR)
#decision tree
button81 =widget.Button()
button81.pack()
button81.place(x=75,y=220)
button81.configure(text="5.Decision tree",bg='darkgoldenrod')
button81.configure(command=DTR)
#random forest
button91 =widget.Button()
button91.pack()
button91.place(x=75,y=250)
button91.configure(text="6.Random Forest",bg='darkgoldenrod')
button91.configure(command=RFR)

#classification
clasl=widget.Label()
clasl.pack()
clasl.configure(text="Classification",fg="lightgreen",bg="blue",font='bold')
clasl.place(x=400,y=60) 


#LogisticRegression
button4 =widget.Button()
button4.pack()
button4.place(x=400,y=100)
button4.configure(text="1.Logistic Regression",bg='mediumpurple')
button4.configure(command=Logi)
#naive bayes
button5 =widget.Button()
button5.pack()
button5.place(x=400,y=130)
button5.configure(text="2.Naive Bayes",bg='mediumpurple')
button5.configure(command=Naive)
#knn
button6 =widget.Button()
button6.pack()
button6.place(x=400,y=160)
button6.configure(text="3.K Nearest Neighbors",bg='mediumpurple')
button6.configure(command=KNN)
#svm
button7 =widget.Button()
button7.pack()
button7.place(x=400,y=190)
button7.configure(text="4.Support Vectore Machine",bg='mediumpurple')
button7.configure(command=SVC)
#decision tree
button8 =widget.Button()
button8.pack()
button8.place(x=400,y=220)
button8.configure(text="5.Decision tree",bg='mediumpurple')
button8.configure(command=DTC)
#random forest
button9 =widget.Button()
button9.pack()
button9.place(x=400,y=250)
button9.configure(text="6.Random Forest",bg='mediumpurple')
button9.configure(command=RFC)
#clustering

regl=widget.Label()
regl.pack()
regl.configure(text="Clustering",fg="lightgreen",bg="blue",font='bold')
regl.place(x=750,y=60) 


#k means
button10 =widget.Button()
button10.pack()
button10.place(x=750,y=100)
button10.configure(text="1.K means cluster",bg='tan')
button10.configure(command=kmeans)
#hirarchical cluster
button20 =widget.Button()
button20.pack()
button20.place(x=750,y=130)
button20.configure(text="2.Hirarchical Cluster",bg='tan')
button20.configure(command=hirarchy)







window.title("choose ml model")
window.geometry("1000x500")
window.configure(bg='blue')
window.mainloop()

