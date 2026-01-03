import pygame 


pygame.init()

#create blank game window
screen_width = 600
screen_height = 600

#create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')


#paddle variables
paddle_width = 100
paddle_height = 20
paddle_speed = 0.6 

#draw rectangle
paddle_x = 270
paddle_y = 570

#draw white circle
ball_x = 322
ball_y = 560
ball_radius = 10

#draw white circle 2
ball_x2 = 270
ball_y2 = 550
ball_radius2 = 10 

#draw red circle
ball_red_x = 320
ball_red_y = 560
ball_radius_red = 10

#draw red circle 2
ball_red_x2 = 320
ball_red_y2 = 560
ball_radius_red_2 = 10 

#white ball movement
x = 0.06
y = -0.06 

#white ball (2) movement
x2 = 0.08
y2 = -0.05

#red ball movement
red_x = -0.08 
red_y = -0.08

#red ball movement (2)
red_x2 = -0.08
red_y2 = -0.05

#draw brick wall
brick_x = 1
brick_y = 1
brick_width = 100
brick_height = 20
rows = 6
columns = 6
spacing = 3


#make paddle
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)



#make white circle balls
pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
pygame.draw.circle(screen, (255, 255, 255), (ball_x2, ball_y2), ball_radius2)

#make red circle balls
pygame.draw.circle(screen, (255, 0, 0), (ball_red_x, ball_red_y), ball_radius_red)
pygame.draw.circle(screen, (255, 0, 0), (ball_red_x2, ball_red_y2), ball_radius_red_2)

#make bricks

bricks = []
for row in range(rows):
    for column in range(columns):
        brick_x = column * (brick_width + spacing)
        brick_y = row * (brick_height + spacing)
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick)


#variables bullets
bullet_width = 10
bullet_height = 20
bullet_x = 316
bullet_y = 570
bullet_speed = -5  

#make bullets
bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)








collide = False
ball_hit_paddle = False
run = True
while run:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        
    #paddle right and barrier screen right 
    keys = pygame.key.get_pressed()        
    if keys[pygame.K_RIGHT]:
        paddle.x += paddle_speed
        bullet.x += paddle_speed
    if paddle.x >= 500:
        paddle.x = 500
    if bullet.x >= 547:
        bullet.x = 547
   
    
    
    
            
    #paddle left and barrier screen left      
    if keys[pygame.K_LEFT]:
        paddle.x -= paddle_speed 
        bullet.x -= paddle_speed
    if paddle.x <= 0:
        paddle.x = 0
    if bullet.x <= 45:
        bullet.x = 45


    #two white balls colliding
    collide = True
    white_circle_1 = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
    white_circle_2 = pygame.draw.circle(screen, (255, 255, 255), (ball_x2, ball_y2), ball_radius2)

    if white_circle_1.colliderect(white_circle_2):
        x = 0.06
        y = 0.06
        x2 = -0.08
        y2 = -0.05
     
     
     
    #paddle colliding with balls
    ball_hit_paddle = True
    white_circle_1 = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
    white_circle_2 = pygame.draw.circle(screen, (255, 255, 255), (ball_x2, ball_y2), ball_radius2)
    red_circle_1 = pygame.draw.circle(screen, (255, 255, 255), (ball_red_x, ball_red_y), ball_radius)
    red_circle_2 = pygame.draw.circle(screen, (255, 255, 255), (ball_red_x2, ball_red_y2), ball_radius2)

    
    if white_circle_1.colliderect(paddle):
        x = -0.06
        y = -0.06
    if white_circle_2.colliderect(paddle):
        x2 = -0.08
        y2 = -0.05
    if red_circle_1.colliderect(paddle):
        red_x = 0.08
        red_y = -0.08
    if red_circle_2.colliderect(paddle):
        red_x2 = 0.08
        red_y2 = -0.05
    


    #bullet fires
    if keys[pygame.K_DOWN]:                                                                            
        bullet.y += bullet_speed 

   
 
    #balls movement
    ball_x += x
    ball_y += y

    if ball_x <= 0 or ball_x >= screen_width:
        x *= -1

    if ball_y <= 0:
        y *= -1
        

    ball_x2 += x2
    ball_y2 += y2
    

    if ball_x2 <= 0 or ball_x2 >= screen_width:
        x2 *= -1

    if ball_y2 <= 0:
        y2 *= -1

    ball_red_x += red_x
    ball_red_y += red_y

    if ball_red_x <= 0 or ball_red_x >= screen_width:
        red_x *= -1

    if ball_red_y <= 0:
        red_y *= -1

    ball_red_x2 += red_x2 
    ball_red_y2 += red_y2  

    if ball_red_x2 <= 0 or ball_red_x2 >= screen_width:
        red_x2 *= -1

    if ball_red_y2 <= 0:
        red_y2 *= -1


   
   

  
 
    
    screen.fill((0, 0, 0)) 

       
    pygame.draw.rect(screen, (255, 255, 0), bullet)   

    pygame.draw.rect(screen, (0, 0, 255), paddle)  # blue paddle
        
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius) 

    pygame.draw.circle(screen, (255, 255, 255), (ball_x2, ball_y2), ball_radius2)

    pygame.draw.circle(screen, (255, 0, 0), (ball_red_x, ball_red_y), ball_radius_red)
    
    pygame.draw.circle(screen, (255, 0, 0), (ball_red_x2, ball_red_y2), ball_radius_red_2)
    
     
 

        

    #creating bricks
    
    for brick in bricks:
        pygame.draw.rect(screen, (0, 0, 255), brick)
                      
    #update the display
    pygame.display.update()

#end pygame
pygame.quit()


#comparisons, if else and booleans for collisions - number 4