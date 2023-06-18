import socket
client_socket=socket.socket()
client_socket.connect(('127.0.0.1',9090))

print ("Клиент работает")
print (client_socket)
while True:

    data=input()
    if data=='q':

        break
    else:client_socket.sendto(bytes(data,encoding='utf-8'),('127.0.0.1',9090))
    msg = client_socket.recv(1024)

    print (msg.decode("UTF-8"))
    #print ('\n')
client_socket.close()










