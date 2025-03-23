import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Drawer")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


running = True
shape = "circle"
color = WHITE
size = 30
shapes = []

def draw_shape(position):
    shapes.append((shape, color, position))


while running:
    screen.fill((0, 0, 0))

    for shape_type, shape_color, pos in shapes:
        if shape_type == "circle":
            pygame.draw.circle(screen, shape_color, pos, size)
        elif shape_type == "rect":
            pygame.draw.rect(screen, shape_color, (pos[0] - size, pos[1] - size, size * 2, size * 2))

    mouse_pos = pygame.mouse.get_pos()
    draw_shape(mouse_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                shapes.clear()
            elif event.key == pygame.K_BACKSPACE:
                if shapes:
                    shapes.pop()
            elif event.key == pygame.K_s:
                shape = "circle"
            elif event.key == pygame.K_e:
                shape = "rect"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE

    pygame.display.flip()

pygame.quit()
