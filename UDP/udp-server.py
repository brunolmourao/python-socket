import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #socket do servidor
s.bind(('localhost', 1234))
requestcount = 0
inicio = time.time()
while True:
    data, adress = s.recvfrom(1024)
    if data:
        requestcount = requestcount +1
        command = data.decode()
        print(f"Server: recived {command}")
        if command == "REQUESTNUM":
            s.sendto(str(requestcount).encode(), adress)
        if command == "UPTIME":
            fim = time.time()
            s.sendto(str(fim-inicio).encode(), adress)

    #s.sendto((data+text.encode()),adress)