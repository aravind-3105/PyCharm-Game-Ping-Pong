import pygame
#iddsnifdsfisdn
from paddle import Paddle
from Ball import Ball
pygame.init()
Blue = (0,0,255)
Black = (0,0,0)
White = (255,255,255)
Yellow = (255,255,0)
Cyan = (0,255,255)

size = (700,500)
display_width = 700
display_height = 500
bg = pygame.image.load('SpaceBackground.png')
Start = pygame.image.load('StartMen.png')

screen = pygame.display.set_mode((display_width,display_height))
#screen = pygame.display.set_mode(size)
pygame.display.set_caption("Modified AirHockey")
#####################################################
Points1 = 0
Points2 = 0
#####################################################
ball = Ball(White,10,10)
ball.rect.x = 345
ball.rect.y = 195
#####################################################
Bat1 = Paddle(Yellow,10,100)
Bat1.rect.x = 0
Bat1.rect.y = 200

Bat2 = Paddle(Yellow,10,100)
Bat2.rect.x = 690
Bat2.rect.y = 200

Objects_Bat_Ball = pygame.sprite.Group()

Objects_Bat_Ball.add(Bat1)
Objects_Bat_Ball.add(Bat2)
Objects_Bat_Ball.add(ball)
######################################################
clock = pygame.time.Clock()
flag = True

def Back(a,x,y):
    screen.blit(a, [x,y])

font = pygame.font.Font("batmfa__.ttf", 75)
StartText = font.render('PING-PONG',True,(255,0,0))
text_rect = StartText.get_rect(center=(350, 200))

font1 = pygame.font.Font("batmfa__.ttf", 24)
StartText1 = font1.render('Press Enter to Start the Game',True,Yellow)
text_rect1 = StartText1.get_rect(center=(350, 300))

font2 = pygame.font.Font("batmfa__.ttf", 24)
StartText2 = font2.render('Press Q to Quit',True,Yellow)
text_rect2 = StartText2.get_rect(center=(350, 350))


font3 = pygame.font.SysFont("comicsansms", 20)
StartText3 = font3.render('Player 1 Controls: W A S D',True,(255,0,0))
text_rect3 = StartText3.get_rect(center=(100, 475))

font4 = pygame.font.SysFont("comicsansms", 20)
StartText4 = font4.render('Player 2 Controls: Arrow Keys',True,(255,0,0))
text_rect4 = StartText4.get_rect(center=(600, 475))

font5 = pygame.font.Font("batmfa__.ttf", 75)
StartText5 = font5.render('PAUSED',True,(255,0,0))
text_rect5 = StartText5.get_rect(center=(350, 200))


#pygame.display.update()
Game_ON = True
###############################################333
while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break
            elif event.key == pygame.K_q:
                pygame.quit()
        Back(Start, 0, 0)

        screen.blit(StartText, text_rect)
        screen.blit(StartText1, text_rect1)
        screen.blit(StartText2, text_rect2)
        screen.blit(StartText3, text_rect3)
        screen.blit(StartText4, text_rect4)
        pygame.display.flip()
        clock.tick(60)
Check_Paused = False
###################################################
while Game_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_ON = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Pressing the x Key will quit the game
                Game_ON = False


  # while flag:
   #        if event.key == pygame.K_r:
    #          flag = False
     #   Back(Start, 0, 0)
    """
    while Check_Paused:
        Back(bg, 0, 0)
        screen.blit(StartText5, text_rect5)
        if pygame.K_c:
            Check_Paused = False
       

    """
    ################################
    Control = pygame.key.get_pressed()
    if Control[pygame.K_w]:
        Bat1.Up(5)
    if Control[pygame.K_s]:
        Bat1.Down(5)
    if Control[pygame.K_UP]:
        Bat2.Up(5)
    if Control[pygame.K_DOWN]:
        Bat2.Down(5)
    """
    if Control[pygame.K_a]:
        Bat1.Left1(5)
    if Control[pygame.K_d]:
        Bat1.Right1(5)
    if Control[pygame.K_LEFT]:
        Bat2.Left2(5)
    if Control[pygame.K_RIGHT]:
        Bat2.Right2(5)
    """
    Objects_Bat_Ball.update()
        ################################
    if ball.rect.x >= 690:
        Points1 += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        Points2 += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]



            ################################
    if pygame.sprite.collide_mask(ball, Bat1) or pygame.sprite.collide_mask(ball, Bat2):
        ball.bounce()

    #screen.fill(Black)
    Back(bg, 0, 0)
    Objects_Bat_Ball.draw(screen)
    ######################################
    # Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(Points1), 1, White)
    screen.blit(text, (250, 10))
    text = font.render(str(Points2), 1, White)
    screen.blit(text, (420, 10))
    ######################################
    pygame.draw.line(screen, Cyan , [349, 0], [349, 500], 5)  #vertical line
    pygame.draw.line(screen, Cyan, [0, 65], [700, 65], 5)     #horizontal line
    pygame.display.flip()
    clock.tick(60)

pygame.quit()