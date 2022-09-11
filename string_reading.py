#the bellow variable takes is containg a string data type 
teststring="my name is ashutosh "
print(teststring)
#in the bellow code we have try to slice the string with the help of this[] it can take three input but ever input will perform different
#task or operation in the string slicing
# like [the the point where we want to start:the point were we want to end:the difference or how many index you want to skip]
#but in negative slicing it works vise-versa
print(teststring[0:5])
print(teststring[0:18:2])
print(teststring[::])
print(teststring[-21:-1])
print(teststring[-21:-1:2])
# in the bellow code the upper means the print the string in complete capital form
print(teststring.upper())
# in the bellow code the lower means the printed string will be in small lettrs format
print(teststring.lower())
# the bellow code will tell the length of the string
print(len(teststring))
#the bellow code can find that the no. of repetation of the word or letter in the complete string
print(teststring.find("a"))
# the bellow code can tell the no. of reprtation of a letter in the string
print(teststring.count("s"))
# the bellow will find wether the code end's with a particular word or character or not
print(teststring.endswith("ashutosh "))
# the bellow code is used to replace a spcific character or word with your desired input
print(teststring.replace("ashutosh","Kim jeha"))
#the bellow code arrange the string in the capital format
print(teststring.capitalize())
#the below code only check alpha in the string not the space or number or other spacial character
print(teststring.isalpha())
# the bellow code is a example of the negative slicing in the string
print(teststring[:-21:-1])