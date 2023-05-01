import pygame, math

# game constants
pygame.init()
WIDTH = 500
HEIGHT = 500
background = "black"
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
PI = 3.1415926

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('PANG')

running = True
# game variables
paddle_left_y = 209
paddle_right_y = 209
velocity_up_down = 10
ball_x = 250
ball_y = 250
ball_change_x = 3
ball_change_y = 1
ball_direction_x = "r"
ball_direction_y = "up"
ball_speed = 5
def ball_update(ball_dir_x, ball_dir_y, ball_c_x, ball_c_y):
    global ball_x, ball_y
    # case 1
    if ball_dir_x == "r" and ball_dir_y == "up":
        ball_x += ball_c_x
        ball_y -= ball_c_y
    # case 2
    elif ball_dir_x == "r" and ball_dir_y == "down":
        ball_x += ball_c_x
        ball_y += ball_c_y
    # case 3
    elif ball_dir_x == "l" and ball_dir_y == "up":
        ball_x -= ball_c_x
        ball_y -= ball_c_y
    # case 4
    elif ball_dir_x == "l" and ball_dir_y == "down":
        ball_x -= ball_c_x
        ball_y += ball_c_y
def ball_switch_x_dir():
    global ball_direction_x
    if ball_direction_x == "r":
        ball_direction_x = "l"
    elif ball_direction_x == "l":
        ball_direction_x = "r"


def ball_switch_y_dir():
    global ball_direction_y

    if ball_direction_y == "up":
        ball_direction_y = "down"

    elif ball_direction_y == "down":
        ball_direction_y = "up"


# def change_angle_collide_bottom(initial_angle):
#     # if collide with paddle or top/bottom
#
#     return final_angle

while running == True:
    timer.tick(fps)
    screen.fill(background)
    keys = pygame.key.get_pressed()



    paddle_left_rect = pygame.Rect(10, paddle_left_y, 10, 82)
    paddle_left_top = pygame.Rect(10, paddle_left_y - 4, 10, 4)
    paddle_left_bottom = pygame.Rect(10, paddle_left_y + 82, 10, 4)
    paddle_right_rect = pygame.Rect(480, paddle_right_y, 10, 82)
    paddle_right_top = pygame.Rect(480, paddle_right_y - 4, 10, 4)
    paddle_right_bottom = pygame.Rect(480, paddle_right_y + 82, 10, 4)

    left_paddle_draw = pygame.draw.rect(screen, "white", paddle_left_rect)
    left_paddle_top_draw = pygame.draw.rect(screen, "red", paddle_left_top)
    left_paddle_bottom_draw = pygame.draw.rect(screen, "blue", paddle_left_bottom)

    right_paddle_draw = pygame.draw.rect(screen, "white", paddle_right_rect)
    right_paddle_top_draw = pygame.draw.rect(screen, "red", paddle_right_top)
    right_paddle_bottom_draw = pygame.draw.rect(screen, "blue", paddle_right_bottom)

    ball_draw = pygame.draw.circle(screen, "white", (ball_x, ball_y), 10)

    if keys[pygame.K_w] and paddle_left_y > 0:
        paddle_left_y -= velocity_up_down
    elif keys[pygame.K_s] and paddle_left_y < 410:
        paddle_left_y += velocity_up_down
    if keys[pygame.K_UP] and paddle_right_y > 0:
        paddle_right_y -= velocity_up_down
    elif keys[pygame.K_DOWN] and paddle_right_y < 410:
        paddle_right_y += velocity_up_down


    if left_paddle_draw.colliderect(ball_draw) or right_paddle_draw.colliderect(ball_draw):
        ball_switch_x_dir()


    if ball_y >= 495 or ball_y <= 5:
        ball_switch_y_dir()

    if left_paddle_top_draw.colliderect(ball_draw):
        print("test")
    ball_update(ball_direction_x, ball_direction_y, ball_change_x, ball_change_y)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()