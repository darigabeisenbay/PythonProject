import pygame
pygame.init()

WIDTH,HEIGHT = 500,500
ball_radius = 25
step = 20
WHITE = (255,255,255)
RED = (255,0,0)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('red_ball🔴')

ball_x,ball_y = WIDTH//2,HEIGHT // 2

running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x  - ball_radius - step >= 0:
        ball_x = ball_x - step
    elif keys[pygame.K_RIGHT] and ball_x + ball_radius + step <= WIDTH:
        ball_x = ball_x + step
    elif keys[pygame.K_UP] and ball_y - ball_radius - step >= 0:
        ball_y = ball_y - step
    elif keys[pygame.K_DOWN] and ball_y + ball_radius + step <= HEIGHT:
        ball_y = ball_y + step

    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,(ball_x,ball_y),ball_radius)
    pygame.display.flip()
pygame.quit()
