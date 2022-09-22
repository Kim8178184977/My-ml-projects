import socket
import datetime
import smtplib
import pickle

address = '127.0.0.1'
port = 5001
soak = socket.socket()

soak.bind((address, port))
soak.listen()
conn, address = soak.accept()

print('connection requst :- '+ str(address))

while True:
    try:
        # for sending and reciving data from the clint
        data = conn.recv(1024).decode()
        if not data:
            break
        data = str(data).upper()
        print ('form user'+str(data))
        conn.send(data.encode())
        data = input('enter the message :- ')
        conn.send(data.encode())
        print('from connection requst :- '+ str(data))
        # for error detection and informing to the server host
        time =  datetime.datetime.now()
        content = f'someone fetching data from server'
        server = smtplib.SMTP('smtp.gmail.com',587)
        mail_id = 'elsarosetop@gmail.com'
        pass_code = 'tcijjurkpgbacajx'
        server.ehlo()
        server.starttls()
        server.login(mail_id,pass_code)
        to_send = 'ashu28jan2003@gmail.com'
        server.sendmail(mail_id,to_send,content)
        server.close()
        my_str1 = f' \n the server was started at {time}'
        with open('server status.txt','a') as file:
            data = file.write(my_str1)
            
    except Exception as e:
        # if there is any error in the code the host will be informed and the error time will be recorded
        server = smtplib.SMTP('smtp.gmail.com',587)
        mail_id = 'elsarosetop@gmail.com'
        pass_code = 'tcijjurkpgbacajx'
        content = f'the server have a problem'
        server.ehlo()
        server.starttls()
        server.login(mail_id,pass_code)
        to_send = 'ashu28jan2003@gmail.com'
        server.sendmail(mail_id,to_send,content)
        server.close()
        print("the server have a problem")
        lis =[]
        my_str = f' \n the server faced a error at {time}'
        with open('server status.txt','a',) as file:
            data1 = file.write(my_str)

    
    
conn.close()
# for pickling the file into binery format

with open('server status.txt','r') as file:
    data = file.read()
with open('server status.txt','r') as file:
    data1 = file.read()

fileobj = open("server data.pcl",'wb')
pickle.dump(data,fileobj)
pickle.dump(data1,fileobj)
fileobj.close()

fileobj1 = open("server status.pcl",'rb')
print(pickle.load(fileobj1))


