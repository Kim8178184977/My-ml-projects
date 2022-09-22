from statistics import linear_regression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as tts
from sklearn.preprocessing import StandardScaler 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score as acc
import matplotlib.pyplot as plt

ss = StandardScaler()

data_set = pd.read_excel("D:\\real life project\Book1.xlsx")


x =data_set.iloc[:,:-1].values

y = data_set.iloc[:,-1].values

x_train,x_test,y_train,y_test = tts(x,y,test_size=0.30,random_state=0)

x_train = ss.fit_transform(x_train)

x_test = ss.transform(x_test)

model = LogisticRegression()

model.fit(x_train,y_train)

y_predict = model.predict(x_test)

print(acc(y_test,y_predict)*100)

age = int(input('enter the age of the coustmer :- '))
sallary = int(input('enter the sallary of the coustmer :- '))

new_cust = [[age,sallary]]

result = model.predict(ss.transform(new_cust))

print(result)

if result == 1:
    print('coustmer will buy the product ')
else:
    print('coustmer will not buy the product')
