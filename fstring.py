#in this code we will learn how to use fstring in the code
# the bellow code is a clasic way to join the srtings it is ok for small data set but ambigues for dig data sets
me = "ashutosh"
n= 19
pre = "I am %s%s"%(me,n)
print(pre)
#the bellow code is a way to join string with str function it is not that ambiguse but hard to read and recquried more un-nessisary line of code
str="I am {}"
print(str.format( "ashutosh 19"))
# the bellow code is a way to call or manupulate a string with the help of f-string
print(f"I am {me}{n}")