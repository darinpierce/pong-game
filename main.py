import pygame

# game constants
pygame.init()
WIDTH = 500
HEIGHT = 500
background = "black"
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()


screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('PANG')

running = True
# game variables
paddle_left_y = 205
paddle_right_y = 205
velocity_up_down = 10
ball_x = 250
ball_y = 250
ball_change_x = 1
ball_change_y = 1
ball_direction_x = False
ball_direction_y = "up"

def ball_update( ball_c_x, ball_c_y):
    global ball_x, ball_y, ball_direction_x, ball_direction_y

    if ball_direction_x == "r" and ball_direction_y == "up":
        ball_x += ball_c_x
        ball_y -= ball_c_y
    if ball_direction_x == "r" and ball_direction_y == "down":
        ball_x += ball_c_x
        ball_y += ball_c_y
    if ball_direction_x == "l" and ball_direction_y == "up":
        ball_x -= ball_c_x
        ball_y -= ball_c_y
    if ball_direction_x == "l" and ball_direction_y == "down":
        ball_x -= ball_c_x
        ball_y += ball_c_y
def ball_switch_x_dir():
    global ball_direction_x
    if ball_direction_x == "r":
        ball_direction_x = "l"
        print("test")
    if ball_direction_x == "l":
        ball_direction_x = "r"


def ball_switch_y_dir():
    global ball_direction_y

    if ball_direction_y == "up":
        ball_direction_y = "down"

    if ball_direction_y == "down":
        ball_direction_y = "up"
    else:
        pass

while running == True:
    timer.tick(fps)
    screen.fill(background)
    keys = pygame.key.get_pressed()



    paddle_left_rect = pygame.Rect(10, paddle_left_y, 10, 90)
    paddle_right_rect = pygame.Rect(480, paddle_right_y, 10, 90)

    left_paddle_draw = pygame.draw.rect(screen, "white", paddle_left_rect)
    right_paddle_draw = pygame.draw.rect(screen, "white", paddle_right_rect)
    ball_draw = pygame.draw.circle(screen, "white", (ball_x, ball_y), 10)

    if keys[pygame.K_w] and paddle_left_y > 0:
        paddle_left_y -= velocity_up_down
    if keys[pygame.K_s] and paddle_left_y < 410:
        paddle_left_y += velocity_up_down
    if keys[pygame.K_UP] and paddle_right_y > 0:
        paddle_right_y -= velocity_up_down
    if keys[pygame.K_DOWN] and paddle_right_y < 410:
        paddle_right_y += velocity_up_down


    if left_paddle_draw.colliderect(ball_draw) or right_paddle_draw.colliderect(ball_draw):
        if ball_direction_x == "r":
            ball_direction_x = "l"
            print("test")
        if ball_direction_x == "l":
            ball_direction_x = "r"

    if ball_y >= 500 or ball_y <= 0:
        # ball_switch_y_dir()
        if ball_direction_x == "r":
            ball_direction_x = "l"

        if ball_direction_x == "l":
            ball_direction_x = "r"

    ball_update(ball_change_x, ball_change_y)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()