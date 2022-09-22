import socket

host = '127.0.0.1'
port = 5001
obj = socket.socket()
obj.connect((host,port))
message = input("type message: ")
while message != 'q':
       try:
              obj.send(message.encode())
              data = obj.recv(1024).decode()
              print ('Received from server: ' + data)
              message = input("type message: ")
       except Exception as e:
              e
              print('the surver is :- ', e)
              break
       
obj.close()

