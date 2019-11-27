import pygame
import tello

pygame.init()
screenWidth = 1080
screenHeight =720
screen = pygame.display.set_mode((screenWidth,screenHeight))
done = False
pressedColor = (0,128,255)
defaultColor = (255,100,0)
clock = pygame.time.Clock()
myTello = tello.Tello()

keyUp = False  #w
keyDown = False #s
keyCcw = False #a
keyCw = False #d
keyFoward = False #i
keyBack = False #k
keyLeft = False #j
keyright = False #l


while not done:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = True
 
    #입력
    pressed = pygame.key.get_pressed()
    #처리
    if pressed[pygame.K_w]:
            keyUp = True
    else:
        keyUp = False

    if pressed[pygame.K_s]:
        keyDown = True
    else:
        keyDown = False
    if pressed[pygame.K_a]:
        keyCcw = True
    else:
        keyCcw = False
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

    #출력
    screen.fill((0,0,0))


    if keyUp:
        pygame.draw.rect(screen,defaultColor,pygame.Rect(screenWidth//3,screenHeight-(screenHeight//3),60,60))#w
    else:
        pygame.draw.rect(screen,pressedColor,pygame.Rect(screenWidth//3,screenHeight-(screenHeight//3),60,60))#w

    if keyDown:
        pygame.draw.rect(screen,defaultColor,pygame.Rect(screenWidth//3,screenHeight-(screenHeight//3)+70,60,60))#s
    else:
        pygame.draw.rect(screen,pressedColor,pygame.Rect(screenWidth//3,screenHeight-(screenHeight//3)+70,60,60))#s
    if keyCcw:
        pygame.draw.rect(screen,defaultColor,pygame.Rect(screenWidth//3 -70,screenHeight-(screenHeight//3)+70,60,60))#a
    else:
        pygame.draw.rect(screen,pressedColor,pygame.Rect(screenWidth//3 -70,screenHeight-(screenHeight//3)+70,60,60))#a
    if keyCw:
        pygame.draw.rect(screen,defaultColor,pygame.Rect(screenWidth//3 +70,screenHeight-(screenHeight//3)+70,60,60))#d
    else:
        pygame.draw.rect(screen,pressedColor,pygame.Rect(screenWidth//3 +70,screenHeight-(screenHeight//3)+70,60,60))#d
        
    if keyFoward:
        pygame.draw.rect(screen,defaultColor,pygame.Rect(screenHeight+(screenWidth//10),screenHeight-(screenHeight//3),60,60))#i
    else:
        pygame.draw.rect(screen,pressedColor,pygame.Rect(screenHeight+(screenWidth//10),screenHeight-(screenHeight//3),60,60))#i
    if keyBack:
        pygame.draw.rect(screen,defaultColor,pygame.Rect(screenHeight+(screenWidth//10),screenHeight-(screenHeight//3)+70,60,60))#k
    else:
        pygame.draw.rect(screen,pressedColor,pygame.Rect(screenHeight+(screenWidth//10),screenHeight-(screenHeight//3)+70,60,60))#k        
    if keyLeft:
        pygame.draw.rect(screen,defaultColor,pygame.Rect(screenHeight+(screenWidth//10)-70,screenHeight-(screenHeight//3)+70,60,60))#k
    else:
        pygame.draw.rect(screen,pressedColor,pygame.Rect(screenHeight+(screenWidth//10)-70,screenHeight-(screenHeight//3)+70,60,60))#k
    if keyRight:
        pygame.draw.rect(screen,defaultColor,pygame.Rect(screenHeight+(screenWidth//10)+70,screenHeight-(screenHeight//3)+70,60,60))#l
    else:
        pygame.draw.rect(screen,pressedColor,pygame.Rect(screenHeight+(screenWidth//10)+70,screenHeight-(screenHeight//3)+70,60,60))#l                                                      

    pygame.display.flip()
    clock.tick(60)   
