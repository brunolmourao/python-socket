import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket do servidor
s.bind(('localhost', 1234))
s.listen(5)
requestcount = 0
inicio = time.time()
while True:
    clientsocket, adress = s.accept()
    print(f"Connection from {adress} has been established")
    while True:
        recebe = clientsocket.recv(1024)
        if not recebe:
            break
        requestcount = requestcount +1
        command = recebe.decode("utf-8")
        print(f"Message recived : {command}")
        if command == "REQUESTNUM":
            msg = str(requestcount)
           # msg = f'{len(msg):<{HEADERSIZE}}' + msg
            clientsocket.send(bytes(msg, "utf-8"))
        if command == "UPTIME":
            fim = time.time()
            msg = str(fim-inicio)
            #msg = f'{len(msg):<{HEADERSIZE}}' + msg
            clientsocket.send(bytes(msg, "utf-8"))