import tello
import time

myTello = tello.Tello()

myTello.sendMsg("command")

myTello.sendMsg("takeoff")
time.sleep(10)

#myTello.up(30)
#time.sleep(5)

#myTello.down(30)
#time.sleep(5)

#myTello.left(30)
#time.sleep(5)

#myTello.cw(30)
#time.sleep(5)

#myTello.ccw(30)
#time.sleep(5)

#myTello.flip("r")
#time.sleep(5)


myTello.sendMsg("mon")

myTello.mdir(0)
time.sleep(1)

myTello.gomid(0,0,100,15,1)
time.sleep(10)

myTello.gomid(30,30,100,15,1)
time.sleep(10)

myTello.gomid(-30,-30,100,15,1)
time.sleep(10)

myTello.gomid(-30,-20,100,15,1)
time.sleep(10)

myTello.gomid(30,-30,100,15,1)
time.sleep(10)

myTello.gomid(0,0,100,15,1)
time.sleep(10)

myTello.sendMsg("land")
print ("Well Done")