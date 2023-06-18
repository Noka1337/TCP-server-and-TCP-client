import socket
import threading
import time


class client_threading(threading.Thread):
    def __init__(self,sock_client,addr_client):
        threading.Thread.__init__(self)
        self.socket_client=sock_client
        self.addr_client=addr_client
        print ("Новое подключение:",sock_client)
        
    def run(self):
        print("Подключен:",self.addr_client)
        self.socket_client.send(b'Options of server: ')
        self.socket_client.send(b' q - Disconnect from server;  ')
        self.socket_client.send(b' hello - Say hello to the server;  ')
        self.socket_client.send(b' Str - Get uppercase string;  ')

        msg=''
        while True:
            data=self.socket_client.recv(1024)
            msg= data.decode("UTF-8")
            if msg=='':
                print (self.addr_client,"- отключился")
                break
            else:
                print (self.addr_client, ":", msg)
            if msg=="hello":
                self.socket_client.send(b'Hello,client ' + bytes(addr_client[0],encoding='utf-8')+ b',' + bytes(str(addr_client[1]),encoding='utf-8') + b'!')
            elif msg=="Str":
                self.socket_client.send(b'Put str')
                strok=str(self.socket_client.recv(1024))
                strokas=strok.upper()
                self.socket_client.send(bytes(str(strokas),encoding='utf-8'))

            else:
                self.socket_client.send(b'Invalid command')



server_socket=socket.socket()
server_socket.bind(('127.0.0.1',9090))
server_socket.listen(3)
print ("Сервер запущен")
print (server_socket)
while True:
    sock_client,addr_client=server_socket.accept()
    new_sock_client=client_threading(sock_client,addr_client)
    new_sock_client.start()

server_socket.close()






