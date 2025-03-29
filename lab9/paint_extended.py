import pygame

pygame.init()

# --- Константы ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Drawer")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

running = True
shapes = []
current_color = BLUE  # Цвет по умолчанию


# --- Функции рисования фигур ---
def draw_circle(position, color, size=30):
    shapes.append(("circle", color, position, size))


def draw_rect(position, color, size=30):
    shapes.append(("rect", color, position, size))


def draw_square(position, color, size=40):
    shapes.append(("square", color, position, size))


def draw_right_triangle(position, color, size=40):
    shapes.append(("right_triangle", color, position, size))


def draw_equilateral_triangle(position, color, size=40):
    shapes.append(("equilateral_triangle", color, position, size))


def draw_rhombus(position, color, size=40):
    shapes.append(("rhombus", color, position, size))


while running:
    screen.fill(BLACK)

    for shape_type, shape_color, pos, size in shapes:
        if shape_type == "circle":
            pygame.draw.circle(screen, shape_color, pos, size)
        elif shape_type == "rect":
            pygame.draw.rect(screen, shape_color, (pos[0] - size, pos[1] - size, size * 2, size * 2))
        elif shape_type == "square":
            pygame.draw.rect(screen, shape_color, (pos[0] - size, pos[1] - size, size, size))
        elif shape_type == "right_triangle":
            pygame.draw.polygon(screen, shape_color,
                                [(pos[0], pos[1]), (pos[0] + size, pos[1]), (pos[0], pos[1] - size)])
        elif shape_type == "equilateral_triangle":
            pygame.draw.polygon(screen, shape_color, [(pos[0], pos[1] - size), (pos[0] - size, pos[1] + size // 2),
                                                      (pos[0] + size, pos[1] + size // 2)])
        elif shape_type == "rhombus":
            pygame.draw.polygon(screen, shape_color,
                                [(pos[0], pos[1] - size), (pos[0] + size, pos[1]), (pos[0], pos[1] + size),
                                 (pos[0] - size, pos[1])])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.key == pygame.K_x:
                shapes.clear()
            elif event.key == pygame.K_BACKSPACE:
                if shapes:
                    shapes.pop()
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_c:
                draw_circle(mouse_pos, current_color)
            elif event.key == pygame.K_r:
                draw_rect(mouse_pos, current_color)
            elif event.key == pygame.K_s:
                draw_square(mouse_pos, current_color)
            elif event.key == pygame.K_t:
                draw_right_triangle(mouse_pos, current_color)
            elif event.key == pygame.K_e:
                draw_equilateral_triangle(mouse_pos, current_color)
            elif event.key == pygame.K_d:
                draw_rhombus(mouse_pos, current_color)

    pygame.display.flip()

pygame.quit()
