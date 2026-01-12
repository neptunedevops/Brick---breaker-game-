import pygame 


pygame.init()

# create blank game window
screen_width = 600
screen_height = 600

# create game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')

# paddle variables
paddle_width = 100
paddle_height = 20
paddle_speed = 0.6 

# draw rectangle
paddle_x = 270
paddle_y = 570

# white balls (starting creation?)
ball_x = 322
ball_y = 560
ball_radius = 10

ball_x2 = 270
ball_y2 = 550
ball_radius2 = 10 

# red balls (starting creation?)
ball_red_x = 320
ball_red_y = 560
ball_radius_red = 10

ball_red_x2 = 320
ball_red_y2 = 560
ball_radius_red_2 = 10 

# ball movement
x, y = 0.06, -0.06 
x2, y2 = 0.08, -0.05
red_x, red_y = -0.08, -0.08
red_x2, red_y2 = -0.08, -0.05

# brick wall (measurements)
brick_width = 100
brick_height = 20
rows = 6
columns = 6
spacing = 3

# 'draw' paddle
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# -------- BRICKS AS DICTIONARIES --------
#this bit is a list
#This loop runs once per row of bricks.
#Then row becomes:
#0, 1, 2, 3, 4, 5
#Each value represents one horizontal row of bricks.
bricks = []
for row in range(rows):
    for column in range(columns):
        brick_x = column * (brick_width + spacing)
        brick_y = row * (brick_height + spacing)


        #"rect" - “Where is this brick on the screen and how big is it?”
        #drawing the brick
        #collision detection

        brick_obj = {
            "rect": pygame.Rect(brick_x, brick_y, brick_width, brick_height),
            "color": (0, 0, 255),   # blue
            "health": 1,
            "active": True
        }
        bricks.append(brick_obj)
#adds this one brick into the list of bricks
# bullets (starting)
bullet = pygame.Rect(316, 570, 10, 20)
bullet_speed = -5  

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # paddle movement
    if keys[pygame.K_RIGHT]:
        paddle.x = paddle.x + paddle_speed
        bullet.x = bullet.x + paddle_speed
    if paddle.x >= 500:
        paddle.x = 500
    if bullet.x >= 547:
        bullet.x = 547
    if keys[pygame.K_LEFT]:
        paddle.x = paddle.x - paddle_speed
        bullet.x = bullet.x - paddle_speed
    if paddle.x <= 0:
        paddle.x = 0
    if bullet.x <= 45:
        bullet.x = 45



   
    
    
    
            
    #paddle left and barrier screen left      
    if keys[pygame.K_LEFT]:
        paddle.x = paddle.x - paddle_speed 
        bullet.x = bullet.x - paddle_speed
    if paddle.x <= 0:
        paddle.x = 0
    if bullet.x <= 45:
        bullet.x = 45

    if keys[pygame.K_DOWN]:
        bullet.y = bullet.y + bullet_speed 

    #two white balls colliding
    #functions need real input and real code.
    # think of function like blob with a wall, you input things in and return outputs
    # There shouldn't be = in inputs  
    collide = True
    circle_1 = pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), ball_radius)
    circle_2 = pygame.draw.circle(screen, (255, 255, 255), (ball_x2, ball_y2), ball_radius2)
    def do_they_collide(circle_1, circle_2):
        return circle_1.colliderect(circle_2)

    if circle_1.colliderect(circle_2):
        x = 0.06
        y = 0.06
        x2 = -0.08
        y2 = -0.05 
     

    # create collision circles
    white_circle_1 = pygame.draw.circle(screen, (255,255,255), (ball_x, ball_y), ball_radius)
    white_circle_2 = pygame.draw.circle(screen, (255,255,255), (ball_x2, ball_y2), ball_radius2)
    red_circle_1   = pygame.draw.circle(screen, (255,255,255), (ball_red_x, ball_red_y), ball_radius_red)
    red_circle_2   = pygame.draw.circle(screen, (255,255,255), (ball_red_x2, ball_red_y2), ball_radius_red_2)

    # paddle collision
    if white_circle_1.colliderect(paddle): y = y * -1
    if white_circle_2.colliderect(paddle): y2 = y2 * -1
    if red_circle_1.colliderect(paddle): red_y = red_y * -1
    if red_circle_2.colliderect(paddle): red_y2 = red_y2 * -1

    # -------- BALLS COLLIDING WITH BRICKS --------
    for brick in bricks:
        if white_circle_1.colliderect(brick["rect"]):
            y = y * -1
            brick["color"] = (255, 0, 0)
            break

        if white_circle_2.colliderect(brick["rect"]):
            y2 = y2 * -1
            brick["color"] = (255, 0, 0)
            break

        if red_circle_1.colliderect(brick["rect"]):
            red_y = red_y * -1
            brick["color"] = (255, 0, 0)
            break

        if red_circle_2.colliderect(brick["rect"]):
            red_y2 = red_y2 * -1
            brick["color"] = (255, 0, 0)
            break

    #balls movement
    ball_x = ball_x + x
    ball_y = ball_y + y

    if ball_x <= 0 or ball_x >= screen_width:
        x = x * -1  

    if ball_y <= 0:
        y = y * -1
        

    ball_x2 = ball_x2 + x2
    ball_y2 = ball_y2 + y2
    

    if ball_x2 <= 0 or ball_x2 >= screen_width:
        x2 = x2 * -1

    if ball_y2 <= 0:
        y2 = y2 * -1

    ball_red_x = ball_red_x + red_x
    ball_red_y = ball_red_y + red_y

    if ball_red_x <= 0 or ball_red_x >= screen_width:
        red_x = red_x * -1

    if ball_red_y <= 0:
        red_y = red_y * -1

    ball_red_x2 = ball_red_x2 + red_x2 
    ball_red_y2 = ball_red_y2 + red_y2  

    if ball_red_x2 <= 0 or ball_red_x2 >= screen_width:
        red_x2 = red_x2 * -1

    if ball_red_y2 <= 0:
        red_y2 = red_y2 * -1


    # -------- DRAW --------
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255,255,0), bullet)
    pygame.draw.rect(screen, (0,0,255), paddle)

    pygame.draw.circle(screen, (255,255,255), (ball_x, ball_y), ball_radius)
    pygame.draw.circle(screen, (255,255,255), (ball_x2, ball_y2), ball_radius2)
    pygame.draw.circle(screen, (255,0,0), (ball_red_x, ball_red_y), ball_radius_red)
    pygame.draw.circle(screen, (255,0,0), (ball_red_x2, ball_red_y2), ball_radius_red_2)

    for brick in bricks:
        pygame.draw.rect(screen, brick["color"], brick["rect"])

    pygame.display.update()

pygame.quit()
