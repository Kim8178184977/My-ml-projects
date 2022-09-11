"""the bellow code is a file inputing code which re-write the code every time we run it"""
# file=open("sample.txt","w")
# file.write("ashutosh is a assassin")
# file.close()
"""the bellow code is to write in the file as a appending input which mean it will not going to rewrite the
whole file it will just make new entry and add the new data at the end of the privious data """
# file=open("sample.txt","a")
# file.write("ashutosh is a assassin\n")
# file.close()
"""the bellow code is to perform both the function together(read and write)"""
file=open("sample.txt","r+")
file.write("ashutosh is a assassin\n")
print(file.read())
file.close()