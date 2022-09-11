import pickle
with open('iris.txt','r') as file:
    data=file.read().split(',')
    
fileobj = open('iris1.pcl','wb')
pickle.dump(data,fileobj)
fileobj.close()

fileobj1= open('iris1.pcl','rb')
data1=pickle.load(fileobj1)
print(data1)