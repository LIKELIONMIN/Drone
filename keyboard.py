import pygame
import tello
pygame.init()
screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode((screenWidth, screenHeight))
done = False
pressedColor = (0, 128, 255)
defaultColor = (255, 100, 0)
clock = pygame.time.Clock()
myTello = tello.Tello()

myTello.sendMsg("command")

telloA = 0
telloB = 0
telloC = 0
telloD = 0

keyUp = False # w
keyDown =False #s
keyCcw =False #a
keyCw =False #d
keyFoward =False #i
keyBack =False #k
keyLeft =False #j
keyRight =False #l

def keyMap():
    global pressed
    global keyUp
    global keyDown
    global keyCcw
    global keyCw
    global keyFoward
    global keyBack
    global keyLeft
    global keyRight
    global telloA
    global telloB
    global telloC
    global telloD
    if pressed[pygame.K_w]: 
        keyUp = True
    else:
        keyUp = False    
    if pressed[pygame.K_s]:
        keyDown = True
    else:
        keyDown = False    

    if pressed[pygame.K_s] and pressed[pygame.K_w]:
        telloC = 0
    elif pressed[pygame.K_w]:
        telloC = 10
    elif pressed[pygame.K_s]:
        telloC = -10
    else:
        telloC = 0

    if pressed[pygame.K_a]:
        keyCcw = True
    else:
        keyCcw = False   

    if pressed[pygame.K_a] and pressed[pygame.K_d]:
        telloD = 0
    elif pressed[pygame.K_d]:
        telloD = 10
    elif pressed[pygame.K_a]:
        telloD = -10
    else:
        telloD = 0

    if pressed[pygame.K_d]:
        keyCw = True
    else:
        keyCw = False    
    if pressed[pygame.K_i]: 
        keyFoward = True
    else:
        keyFoward = False    
    if pressed[pygame.K_k]:
        keyBack = True
    else:
        keyBack = False    
    if pressed[pygame.K_j]:
        keyLeft = True
    else:
        keyLeft = False    
    if pressed[pygame.K_l]:
        keyRight = True
    else:
        keyRight = False    

myTello.sendMsg("takeoff")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #입력
    pressed = pygame.key.get_pressed()

    #처리
    keyMap()

    #출력
    screen.fill((0, 0, 0))
    
    if keyUp:
        pygame.draw.rect(screen, defaultColor, 
            pygame.Rect(screenWidth//3, screenHeight-(screenHeight//3), 60, 60)) #w
    else: 
        pygame.draw.rect(screen, pressedColor, 
            pygame.Rect(screenWidth//3, screenHeight-(screenHeight//3), 60, 60)) #w
    
    if keyDown:
        pygame.draw.rect(screen, defaultColor, 
            pygame.Rect(screenWidth//3, screenHeight-(screenHeight//3)+70, 60, 60)) #s
    else: 
        pygame.draw.rect(screen, pressedColor, 
            pygame.Rect(screenWidth//3, screenHeight-(screenHeight//3)+70, 60, 60)) #s

    if keyCcw:
        pygame.draw.rect(screen, defaultColor, 
            pygame.Rect(screenWidth//3-70, screenHeight-(screenHeight//3)+70, 60, 60)) #s
    else: 
        pygame.draw.rect(screen, pressedColor, 
            pygame.Rect(screenWidth//3-70, screenHeight-(screenHeight//3)+70, 60, 60)) #s

    if keyCw:
        pygame.draw.rect(screen, defaultColor, 
            pygame.Rect(screenWidth//3+70, screenHeight-(screenHeight//3)+70, 60, 60)) #s
    else: 
        pygame.draw.rect(screen, pressedColor, 
            pygame.Rect(screenWidth//3+70, screenHeight-(screenHeight//3)+70, 60, 60)) #s

    if keyFoward:
        pygame.draw.rect(screen, defaultColor, 
            pygame.Rect(screenWidth- (screenWidth//3), screenHeight-(screenHeight//3), 60, 60)) #s
    else: 
        pygame.draw.rect(screen, pressedColor, 
            pygame.Rect(screenWidth- (screenWidth//3), screenHeight-(screenHeight//3), 60, 60)) #s

    if keyBack:
        pygame.draw.rect(screen, defaultColor, 
            pygame.Rect(screenWidth- (screenWidth//3), screenHeight-(screenHeight//3)+70, 60, 60)) #s
    else: 
        pygame.draw.rect(screen, pressedColor, 
            pygame.Rect(screenWidth- (screenWidth//3), screenHeight-(screenHeight//3)+70, 60, 60)) #s

    if keyLeft:
        pygame.draw.rect(screen, defaultColor, 
            pygame.Rect(screenWidth- (screenWidth//3)-70, screenHeight-(screenHeight//3)+70, 60, 60)) #s
    else: 
        pygame.draw.rect(screen, pressedColor, 
            pygame.Rect(screenWidth- (screenWidth//3)-70, screenHeight-(screenHeight//3)+70, 60, 60)) #s

    if keyRight:
        pygame.draw.rect(screen, defaultColor, 
            pygame.Rect(screenWidth- (screenWidth//3)+70, screenHeight-(screenHeight//3)+70, 60, 60)) #s
    else: 
        pygame.draw.rect(screen, pressedColor, 
            pygame.Rect(screenWidth- (screenWidth//3)+70, screenHeight-(screenHeight//3)+70, 60, 60)) #s

    rcCmd = "rc " + str(telloA) + " "+ str(telloB) + " " + str(telloC) + " " + str(telloD)
    myTello.sendMsg(rcCmd)
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #s
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #a
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #d
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #i
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #k
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #j
    # pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60)) #l
    pygame.display.flip()
    clock.tick(60)

