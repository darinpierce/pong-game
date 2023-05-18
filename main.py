import pygame, math, random

# game constants
pygame.init()
WIDTH = 500
HEIGHT = 500
background = "black"
fps = 60
font_1 = pygame.font.Font('freesansbold.ttf', 32)
font_2 = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
PI = 3.1415926


screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('PANG')

game_start = False
running = True
# game variables

paddle_length = 82
paddle_left_y = HEIGHT / 2 - (paddle_length / 2)
paddle_right_y = HEIGHT / 2 - (paddle_length / 2)
velocity_up_down = 10
ball_x = 250
ball_y = 250

ball_angle = 30
ball_speed = 3


ball_direction_x = "l"
ball_direction_y = "up"
ball_speed = 5

right_points = 0
left_points = 0


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


while running == True:
    timer.tick(fps)
    screen.fill(background)
    keys = pygame.key.get_pressed()

    ball_change_x = math.cos(ball_angle * (PI / 180)) * ball_speed
    ball_change_y = math.sin(ball_angle * (PI / 180)) * ball_speed * -1


    left_score_render = font_1.render(str(left_points), True, "white")
    right_score_render = font_1.render(str(right_points), True, "white")
    start_text_render = font_1.render("PRESS SPACE", True, "white")
    keys_left_render = font_2.render("Move with W and S", True, "white")
    keys_right_render = font_2.render("Move with UP and DOWN", True, "white")

    left_score_rect = left_score_render.get_rect()
    left_score_rect.center = (WIDTH / 3, 25)
    right_score_rect = right_score_render.get_rect()
    right_score_rect.center = ((WIDTH / 3) * 2, 25)

    keys_left_rect = keys_left_render.get_rect()
    keys_left_rect.center = (WIDTH / 4, HEIGHT / 2 - 30)
    keys_right_rect = keys_right_render.get_rect()
    keys_right_rect.center = (WIDTH / 4 * 3, HEIGHT / 2 - 30)

    start_text_rect = start_text_render.get_rect()
    start_text_rect.center = (WIDTH / 2 , HEIGHT / 2 + 20)

    screen.blit(left_score_render, left_score_rect)
    screen.blit(right_score_render, right_score_rect)
    if not game_start:
        screen.blit(start_text_render, start_text_rect)
        screen.blit(keys_left_render, keys_left_rect)
        screen.blit(keys_right_render, keys_right_rect)
    paddle_left_rect = pygame.Rect(10, paddle_left_y, 10, paddle_length)
    paddle_right_rect = pygame.Rect(480, paddle_right_y, 10, paddle_length)

    midline_rect = pygame.Rect((WIDTH / 2) - 1, 0, 2, 500)
    midline_draw = pygame.draw.rect(screen, "white", midline_rect)

    left_paddle_draw = pygame.draw.rect(screen, "white", paddle_left_rect)
    right_paddle_draw = pygame.draw.rect(screen, "white", paddle_right_rect)


    ball_draw = pygame.draw.circle(screen, "white", (ball_x, ball_y), 10)

    if keys[pygame.K_SPACE]:
        game_start = True

    if game_start:
        if keys[pygame.K_w] and paddle_left_y > 0:
            paddle_left_y -= velocity_up_down
        elif keys[pygame.K_s] and paddle_left_y < 410:
            paddle_left_y += velocity_up_down
        if keys[pygame.K_UP] and paddle_right_y > 0:
            paddle_right_y -= velocity_up_down
        elif keys[pygame.K_DOWN] and paddle_right_y < 410:
            paddle_right_y += velocity_up_down


        if left_paddle_draw.colliderect(ball_draw) and ball_direction_x == "l" and 15 < ball_x:
            # hits top going up
            if ball_y <= paddle_left_y + paddle_length/3 and ball_direction_y == "up" and 20 <= ball_angle:
                ball_angle -= 20
                print(str(ball_angle) + " - 20")
                ball_switch_x_dir()
            # hits top going down
            elif ball_y <= paddle_left_y + paddle_length/3 and ball_direction_y == "down" and ball_angle <= 50:
                ball_angle += 20
                print(str(ball_angle) + " + 20")

            # hits bottom going up
            elif paddle_left_y + ((paddle_length/3)*2) <= ball_y <= paddle_left_y + paddle_length and ball_direction_y == "up" and ball_angle <= 50:
                ball_angle += 20
                print(str(ball_angle) + " + 20")

            # hits bottom going down
            elif paddle_left_y + ((paddle_length/3) * 2) <= ball_y <= paddle_left_y + paddle_length and ball_direction_y == "down" and 20 <= ball_angle:
                ball_angle -= 20
                print(str(ball_angle) + " - 20")

            # hits middle
            elif paddle_left_y + paddle_length/3 <= ball_y <= paddle_left_y + (paddle_length / 3) * 2:
                print(str(ball_angle) + " =")


            ball_switch_x_dir()
            print(ball_direction_x)
        if right_paddle_draw.colliderect(ball_draw) and ball_direction_x == "r" and ball_x < 485:
            # hits top going up
            if ball_y <= paddle_right_y + paddle_length / 3 and ball_direction_y == "up" and 20 <= ball_angle:
                ball_angle -= 20
                print(str(ball_angle) + " - 20")

            # hits top going down
            elif ball_y <= paddle_right_y + paddle_length / 3 and ball_direction_y == "down" and ball_angle <= 50:
                ball_angle += 20
                print(str(ball_angle) + " + 20")

            # hits bottom going up
            elif paddle_right_y + ((paddle_length / 3) * 2) <= ball_y <= paddle_right_y + paddle_length and ball_direction_y == "up" and ball_angle <= 50:
                ball_angle += 20
                print(str(ball_angle) + " + 20")

            # hits bottom going down

            elif paddle_right_y + (paddle_length / 3) * 2 <= ball_y <= paddle_right_y + paddle_length and ball_direction_y == "down" and 20 <= ball_angle:
                ball_angle -= 20
                print(str(ball_angle) + " - 20")

            # hits middle
            elif paddle_right_y + paddle_length / 3 <= ball_y <= paddle_right_y + (paddle_length / 3) * 2:
                print(str(ball_angle) + " =")

            ball_switch_x_dir()
            print(ball_direction_x)


        if ball_y >= 495 or ball_y <= 5:
            ball_switch_y_dir()

        if ball_x <= 5:
            right_points += 1
            ball_x = WIDTH / 2
            ball_y = HEIGHT / 2
            ball_angle = random.randrange(0, 70, 1)
        elif ball_x >= 495:
            left_points += 1
            ball_x = WIDTH / 2
            ball_y = HEIGHT / 2
            ball_angle = random.randrange(0, 70, 1)

        ball_update(ball_direction_x, ball_direction_y, ball_change_x, ball_change_y)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()