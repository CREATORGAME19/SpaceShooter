version = "1.1"
print('Spaceshooter V'+version)
print('#####Changelog#####')
print('Added pause screen and fixed bugs')
print('')
print ('If you see a error in this window please make sure you have pygame installed')
x = 200
y = 400
x1 = 0
y1 = 0
x2 = 0
y2 = 0
x3 = 0
y3 = 0
ly1 = 0
lx1 = 0
shot1 = 0
recharge = 0
counter = 0
rechargecounter = 0
gone1=0
gone2=0
gone3=0
useless=0
pause=True
custom = False # Customises the difficulty if True
if (custom == True):
    difficulty = input("Enter the difficulty you want (250-super easy, 400-normal, 600-hard, 1000 ARE YOU INSANE!)")
    if(int(difficulty)<250):
        difficulty = 250
else:
    difficulty = 400

import random
import pygame
import sys
pygame.init()
window= pygame.display.set_mode((500,500))
pygame.display.set_caption('Game')
white = (255,255,255)
background = pygame.image.load('Images/Background2.png')
image = pygame.image.load('Images/spaceship.png')
meteor = pygame.image.load('Images/Asteroid.png')
lazer = pygame.image.load('Images/L1.png')
rechargeicon = pygame.image.load('Images/Tick.png')
useless1 = pygame.image.load('Images/L1.png')
screen = 0
gameLoop = True  
    
while gameLoop:
    
    if(y1 >= 500 or gone1 == 1):
            x1 = random.randint(1,501)
            y1 = 0
            gone1=0
            
    elif(y2 >= 500 or gone2 == 1):
            x2 = random.randint(1,501)
            y2 = 0
            gone2=0
    elif(y3 >= 500 or gone3 == 1):
            x3 = random.randint(1,501)
            y3 = 0
            gone3=0
    
    elif(shot1 == 1 and recharge == 0):
            if(ly1 <= 0 ):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  lx1 = 0
                  ly1 = 0
                  
            elif(x1+40>=lx1>=x1 and y1+40>=ly1>=y1):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone1=1
                  lx1 = 0
                  ly1 = 0
            elif(x1+40>=lx1+2.5>=x1 and y1+40>=ly1>=y1):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone1=1
                  lx1 = 0
                  ly1 = 0
            elif(x1+40>=lx1>=x1 and y1+40>=ly1+30>=y1):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone1=1
                  lx1 = 0
                  ly1 = 0
            elif(x1+40>=lx1+2.5>=x1 and y1+40>=ly1+25>=y1):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone1=1
                  lx1 = 0
                  ly1 = 0
            elif(x2+40>=lx1>=x2 and y2+40>=ly1>=y2):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone2=1
                  lx1 = 0
                  ly1 = 0
            elif(x2+40>=lx1+2.5>=x2 and y2+40>=ly1>=y2):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone2=1
                  lx1 = 0
                  ly1 = 0
            elif(x2+40>=lx1>=x2 and y2+40>=ly1+30>=y2):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone2=1
                  lx1 = 0
                  ly1 = 0
            elif(x2+40>=lx1+2.5>=x2 and y2+40>=ly1+25>=y2):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone2=1
                  lx1 = 0
                  ly1 = 0
            elif(x3+40>=lx1>=x3 and y3+40>=ly1>=y3):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone3=1
                  lx1 = 0
                  ly1 = 0
            elif(x3+40>=lx1+2.5>=x3 and y3+40>=ly1>=y3):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone3=1
                  lx1 = 0
                  ly1 = 0
            elif(x3+40>=lx1>=x3 and y3+40>=ly1+30>=y3):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone3=1
                  lx1 = 0
                  ly1 = 0
            elif(x3+40>=lx1+2.5>=x3 and y3+40>=ly1+25>=y3):
                  lazer = pygame.image.load('Images/L1.png')
                  shot1 = 0
                  recharge = 1
                  gone3=1
                  lx1 = 0
                  ly1 = 0
            else:
                  ly1 = ly1 - 20
    elif(rechargecounter + int(difficulty) == counter and recharge == 1):
            recharge = 0
            rechargeicon = pygame.image.load('Images/Tick.png')

    elif(x1+40>=x>=x1 and y1+40>=y>=y1):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x1+40>=x+40>=x1 and y1+40>=y>=y1):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x1+40>=x>=x1 and y1+40>=y+40>=y1):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x1+40>=x+40>=x1 and y1+40>=y+40>=y1):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x2+40>=x>=x2 and y2+40>=y>=y2):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x2+40>=x+40>=x2 and y2+40>=y>=y2):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x2+40>=x>=x2 and y2+40>=y+40>=y2):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x2+40>=x+40>=x2 and y2+40>=y+40>=y2):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x3+40>=x>=x3 and y3+40>=y>=y3):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x3+40>=x+40>=x3 and y3+40>=y>=y3):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x3+40>=x>=x3 and y3+40>=y+40>=y3):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(x3+40>=x+40>=x3 and y3+40>=y+40>=y3):
            gameLoop = False
            pygame.quit()
            print("Game over")
            print("Your score is ",counter)
    elif(pause == True):
            useless=useless+1
            screen= pygame.image.load('Images/screen.jpg')
            sx = 85
            sy = 100
            if(useless>500):
                useless = 0
            
    else:
            screen = pygame.image.load('Images/L1.png')
            sx = 0
            sy = 0
            y1 = y1+((counter/10000)+((int(difficulty)/100)-1))
            y2 = y2+((counter/10000)+((int(difficulty)/100)-1))
            y3 = y3+((counter/10000)+((int(difficulty)/100)-1))
            
    
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
           gameLoop = False

        elif(event.type == pygame.MOUSEBUTTONDOWN and shot1 == 0 and recharge == 0 and pause == False):
            shot1 = 1
            lx1 = x
            ly1 = y
            lazer = pygame.image.load('Images/Lazer.png')
            rechargeicon = pygame.image.load('Images/Tick_red.png')
            rechargecounter = counter
        elif(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_SPACE):
                pause = True
         
        elif(event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN and pause == True):
            pause = False
        else:
            if(pause == False):
                counter = counter + 1
                mx,my = pygame.mouse.get_pos()
                x = mx - 40
            
                        
               
                        
     
    window.fill(white)
    window.blit(background,(0,0))
    window.blit(image,(x,y))
    window.blit(meteor,(x1,y1))
    window.blit(meteor,(x2,y2))
    window.blit(meteor,(x3,y3))
    window.blit(lazer,(lx1,ly1))
    window.blit(rechargeicon,(15,10))
    window.blit(useless1,(0,useless))
    window.blit(screen,(sx,sy))
    pygame.display.update()
pygame.quit()




    

