import socket
from win10toast import ToastNotifier

#initialise socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    #establish conncctions
    clientsocket, address = s.accept()
    print(f"Connection from {address} established.")
    clientsocket.send(bytes("Connection to server established","utf-8"))

    #receive message from client
    reply=clientsocket.recv(4096)
    reply=str(reply)[1:]

    #convert to toast
    notifier=ToastNotifier()
    notifier.show_toast("Alert",reply)

    #terminate
    clientsocket.close()
