import threading
import socket
import sys


class Tello:

    host = ''
    port = 9000
    locaddr = (host, port)

    def __init__(self):
        self.tello_address = ('192.168.10.1', 8889)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)
        self.recvThread = threading.Thread(target=self.recv)
        self.recvThread.start()

    def recv(self):
        while True: 
            try:
                data, server = self.sock.recvfrom(1518)
                print(data.decode(encoding="utf-8"))

            except Exception:
                print ('\nExit . . .\n')
                break

    def sendMsg(self, msg):
        msg = msg.encode(encoding="utf-8")
        self.sock.sendto(msg, self.tello_address)
        print("Sending Command" + str(msg))

    def telloCommnad(self):
        self.sendMsg("command")
        print("Online")

    def up(self, x):
        if x> 500 :
            x= 500
        if x< 20:
            x= 20
        self.sendMsg("up " + str(x)) 

    def down(self, x):
        if x> 500 :
            x= 500
        if x< 20:
            x= 20
        self.sendMsg("down " + str(x)) 
