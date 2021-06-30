#SMILEY PONG version 4.0
import pygame
pygame.init()
screen = pygame.display.set_mode([1500,800])
pygame.display.set_caption("SMILEY PONG version 4.0")
keepGoing=True

pic=pygame.image.load("CrazySmile.bmp")
#colorkey=pic.get_at((0,0))
#pic.set_colorkey(colorkey)
picx=0
picy=0
BLACK=(255,255,255)
BLUE=(0,0,255)
timer=pygame.time.Clock()
speedx=10
speedy=10
paddlew=200
paddleh=25
paddlex=300
paddley=550
picw=100
pich=100
points=0
lives=1
font=pygame.font.SysFont("Times", 24)

while keepGoing:
    for event in pygame.event.get():
         if lives<1:
             print("YOU LOSE!!")
             #pygame.quit()
             points=0
             lives=1
         if event.type==pygame.QUIT:
            keepGoing=False
        
    picx += speedx
    picy += speedy

    if picx<=0 or picx+pic.get_width()>=1500:
        speedx = -speedx
    if picy<=0:
       speedy= -speedy
    if picy>=500:
        lives -= 1
        speedy=-speedy

    screen.fill(BLUE)
    screen.blit(pic,(picx, picy))

    paddlex=pygame.mouse.get_pos()[0]
    paddlex-=paddlew/2
    pygame.draw.rect(screen, BLACK, (paddlex, paddley, paddlew, paddleh))

    if picy+pich>= paddley and picy+pich<=paddley+paddleh \
    and speedy>0:
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + \
           paddlew:
            points +=1
            speedy=-speedy

    draw_string = "Lives: " + str(lives) + "Points: " + str(points)  

    text=font.render(draw_string, True, BLACK)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)
    pygame.display.update()
    timer.tick(60)

pygame.quit()

       



