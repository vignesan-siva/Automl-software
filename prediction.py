
i=[0]
d=[1]
m=56
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np
filename=askopenfilename()
data=pd.read_csv(filename)
x=data.iloc[:,i]
y=data.iloc[:,d]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)
pred=reg.predict([[m]])
from sklearn.metrics import r2_score
accuracy=r2_score(y_test,y_pred)
print("prediction value",+pred)



