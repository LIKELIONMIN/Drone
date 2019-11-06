import tello
import time

myTello = tello.Tello()

myTello.telloCommnad
myTello.sendMsg("takeoff")
time.sleep(10)
myTello.sendMsg("land")
print ("Well Done")