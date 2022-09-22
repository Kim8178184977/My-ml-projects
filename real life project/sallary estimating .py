import pandas as pd
import numpy as nu
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier 
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import accuracy_score as acc

error = []

data_set = pd.read_excel('D:\\real life project\sallary.xlsx')

income_set = set(data_set['income'])
data_set['income'] = data_set['income'].map({'=<50k':0,'>50k':1}).astype(int)

x = data_set.iloc[:,:-1].values

y = data_set.iloc[:,-1].values

x_train,x_test,y_train,y_test = tts(x,y,test_size=0.30,random_state=0)

sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

for i in range (1,40):
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(x_train,y_train)
    prid_i = model.predict(x_test)
    error.append(nu.mean(prid_i != y_test))

r=acc(y_test,prid_i)
print(r*100)
plt.figure(figsize=(12,6))
plt.plot(error,color='red',linestyle = 'dashed',marker = 'o',markerfacecolor = 'blue', markersize=10)
plt.title('error rate ')
plt.xlabel('k vlaue')
plt.ylabel('Mean error')

plt.show()
