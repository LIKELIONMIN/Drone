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
        self.recvThread = threading.Thread(target=self.recv, daemon=True)
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
        print(msg)
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

    def left(self, x):
        if x> 500 :
            x= 500
        if x< 20:
            x= 20
        self.sendMsg("left " + str(x))

    def right(self, x):
        if x> 500 :
            x= 500
        if x< 20:
            x= 20
        self.sendMsg("right " + str(x))

    def cw(self, x):
        if x> 360 :
            x= 360
        if x< 1:
            x= 1
        self.sendMsg("cw " + str(x))

    def ccw(self, x):
        if x> 360 :
            x= 360
        if x< 1:
            x= 1
        self.sendMsg("ccw " + str(x)) 

    def flip(self, x):
        if x=="r" or x=="l" or x=="f" or x=="b":
             self.sendMsg("flip " + x)
       

    def mon(self):
        self.sendMsg("mon")
    
    def moff(self):
        self.sendMsg("moff")

    def mdir(self, x):
        if x == 0: # 0 이면 아래방향
            self.sendMsg("mdirection 0")
        if x == 1: # 1이면 앞방향
            self.sendMsg("mdirection 1")            
        if x == 2: # 2면 둘다
            self.sendMsg("mdirection 2")
        
    def gomid(self, x, y, z, speed, mid):
        if x>500 :
            x=500
        if x< -500 :
            x=-500
        if y>500 :
            y=500
        if y< -500 :
            y=-500
        
        if z>500 :
            z=500
        if z< -500 :
            z=-500   
        #Speed 범위 조정
        if speed> 100 :
            speed=100
        if x< 10 :
            x=10
        #미션패드의 번호에 따라 명령 보냄    
        self.sendMsg("go " 
            + str(x) + " " 
            + str(y) + " " 
            + str(z) + " " 
            + str(speed) + " " 
            + "m"+ str(mid))                                              



      