import tello
import time

myTello = tello.Tello()

myTello.sendMsg("command")
time.sleep(10)
myTello.sendMsg("takeoff")
time.sleep(10)

myTello.up(10)
time.sleep(5)

#myTello.down(50)
#time.sleep(5)


#myTello.left(30)
#time.sleep(5)

#myTello.right(50)
#time.sleep(5)


#myTello.cw(300)
#time.sleep(10)

#myTello.ccw(360)
#time.sleep(10)

#myTello.flip("r")
#time.sleep(5)

#myTello.flip("l")
#time.sleep(5)

#myTello.flip("f")
#time.sleep(5)

#myTello.flip("b")
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