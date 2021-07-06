import pygame, sys, random, os, threading, playsound
from pygame import mixer
from playsound import playsound
from pygame import event
mixer.init()
pygame.init()
#Multithreading Functions
def task1():
    mixer.music.load("Hit.mp3")
    mixer.music.set_volume(5)
    mixer.music.play()
def task2():
    mixer.music.load("Lose.mp3")
    mixer.music.set_volume(0.25)
    mixer.music.play()

def music():
    playsound("Background.mp3")
def gameover():
    mixer.music.load("Game Over.mp3")
    mixer.music.set_volume(1)
    mixer.music.play()


#Setting Up Window
gameIcon = pygame.image.load('Ball.ico')
pygame.display.set_icon(gameIcon)
from pygame.constants import RESIZABLE
pygame.init()
screen = pygame.display.set_mode((1200,800), RESIZABLE)
pygame.display.set_caption("Ping Pong 9.0")
white = (255, 255, 255)
X = 1920
Y = 1080
image = pygame.image.load(r'Space.jpg')
width = screen.get_width()
height = screen.get_height()
keepGoing=True
keepStopping=False
pic=pygame.image.load("Ball.png")
#colorkey=pic.get_at((0,0))
#pic.set_colorkey(colorkey)
picx=0
picy=0
BLACK=(0,0,0)
BLUE=(89,127,143)
GREY = (91,91,91) 
timer=pygame.time.Clock()
#Important
speedx=5
speedy=5
#Important
paddlew=100
paddleh=25
paddlex=300
paddley=height-50
picw=100
pich=100
points=0
lives=3
font=pygame.font.SysFont("Segoe UI", 24)
music = threading.Thread(target=music, name='music')
music.start()
while keepGoing:
    paddley=height-50
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
            keepGoing=False
            
         if event.type==pygame.KEYDOWN:
             if event.key==pygame.K_SPACE:
                 points=0
                 imagex= random.randint(6,11)
                 imagey = random.randint(5,10)
                 lives=3
                 picx=0
                 picy=0
                 speedx=imagex
                 speedy=imagey
    width = screen.get_width()
    height = screen.get_height()
    screen.fill(white)
    screen.blit(image, (0,0))
    
    
    
    picx += speedx
    picy += speedy
    imagex= random.randint(6,11)
    imagey = random.randint(5,10)
    if picx<=0 or picx+pic.get_width()>=(width):
        speedx = -speedx*1.1
    if picy<=0:
       speedy= -speedy+1
    if picy>=(height):
        lives -=1
        t2 = threading.Thread(target=task2, name='t2')  
        t2.start()
        speedy=-imagey
        speedx=imagex
        picy=499
    

    #screen.fill(BLUE)
    screen.blit(pic,(picx, picy))

    paddlex=pygame.mouse.get_pos()[0]
    paddlex-=paddlew/2
    #Important
    pygame.draw.rect(screen, GREY, (paddlex, paddley, paddlew, paddleh))
    #Important
    if picy+pich>= paddley and picy+pich<=paddley+paddleh \
    and speedy>0:
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + \
           paddlew:
            points +=5
            t1 = threading.Thread(target=task1, name='Jump Sound')
            t1.start()
            speedy=-speedy
    draw_string = "Lives: " + str(lives) + " Points: " + str(points)

    if lives==0:
        t2 = threading.Thread(target=task2, name='t2')
        speedx=speedy=0
        draw_string="Game Over. Your score was: "+str(points)
        draw_string+=". Press SPACE to play again. "
        gameover = threading.Thread(target=gameover, name='Game Over')
        gameover.start()
    

    text=font.render(draw_string, True, white)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y = 14
    screen.blit(text, text_rect)
    pygame.display.update()
    timer.tick(60)

width = screen.get_width()
height = screen.get_height()

pygame.quit()
os.system(' cmd /k "TASKKILL /IM "python.exe" /F"')
os.system('  cmd /k "TASKKILL /IM "cmd.exe" /F"')