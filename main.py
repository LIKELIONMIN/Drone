import tello
import time

myTello = tello.Tello()

myTello.sendMsg("command")
myTello.sendMsg("takeoff")
time.sleep(10)
myTello.sendMsg("land")
print ("Well Done")