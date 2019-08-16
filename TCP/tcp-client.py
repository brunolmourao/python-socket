import socket
print("Welcome to ATV1, which server do you want to connect?")
server = input()
print("Which port do you want to connect?")
port = input()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = int(port)
s.connect((server, port))

while True:
    message = input("Type one of these commands:\n1- REQUESTNUM \n2-UPTIME \n3-CLOSE")
    if message == "CLOSE":
        s.send(bytes(message, "utf-8"))
        s.shutdown(1)
        s.close()
        break
    else:
        s.send(bytes(message, "utf-8"))
    new_msg = True
    while new_msg:
        msg = s.recv(1024)
        print(msg.decode("utf-8"))
        new_msg = False