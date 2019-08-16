import socket
print("Welcome to ATV1, which server do you want to connect?")
host = input()
print("Which port do you want to connect?")
port = input()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(port)
while True:
    message = input("Type one of these commands:\n1- REQUESTNUM \n2-UPTIME \n3-CLOSE")
    if message == "CLOSE":
        print("Closing Connection...")
        s.close()
    #print('Client:' + message)
    s.sendto(message.encode(), (host, port))
    data, server = s.recvfrom(1024)
    data = data.decode()
    print(data)
