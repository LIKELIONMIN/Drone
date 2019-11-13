import tello
import time

myTello = tello.Tello()

myTello.sendMsg("command")

myTello.sendMsg("takeoff")
time.sleep(10)

myTello.up(30)
time.sleep(5)

myTello.down(30)
time.sleep(5)

myTello.left(30)
time.sleep(5)

myTello.cw(30)
time.sleep(5)

myTello.ccw(30)
time.sleep(5)


myTello.sendMsg("land")
print ("Well Done")