import os
#the bellow function is to get the loction of the file you are currently working on 
print(os.getcwd())
#the bellow function will change the directery from where you were working from
os.chdir("D:\\")
print(os.getcwd())
#the bellow code will give you the name of the files present in the directory in the form of list
print(os.listdir())
#the bellow code will change the name of file **note:-(initial name , new name)
os.rename("oppai.jpg","Highschool-DxD.jpg")#inter chanege the name before running the program
print(os.listdir())
print(os.getcwd())
