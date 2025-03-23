import pygame, sys
from pygame.locals import *
import random, time
import os

pygame.init()

# --- Константы ---
FPS = 40
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ROAD_LEFT = 50
ROAD_RIGHT = 350
SPEED = 5
SCORE = 0
dodged_cars = 0
COINS_COLLECTED = 0  # Счетчик монет

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# --- Шрифты ---
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# --- Окно игры ---
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

#Загрузка звука
crash_sound = pygame.mixer.Sound(os.path.join(os.path.expanduser("~"), 'Desktop', "crash.wav"))


# --- Класс врагов (машины) ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw_image = pygame.image.load(os.path.join(os.path.expanduser("~"), 'Desktop', "Enemy.png"))
        self.image = pygame.transform.scale(raw_image, (60, 100))
        self.rect = self.image.get_rect()
        self.reset_position()

    def update(self):
        self.rect.y += self.speed  # Тут управляется скорость врага
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_position()

    def reset_position(self):
        """Переспавнить врага в случайном месте сверху"""
        self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), -random.randint(50, 150))

    def move(self):
        """Двигает машину вниз. Если она уходит за экран, она переспавнится сверху."""
        global dodged_cars, SCORE, previous_dodged_cars  # Глобальные переменные

        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            dodged_cars += 1  # Увеличиваем счетчик увернутых машин
            self.reset_position()  # Переспавниваем машину сверху

            # Если машина увернута, увеличиваем общий SCORE
            if dodged_cars > previous_dodged_cars:
                SCORE += 1
                previous_dodged_cars = dodged_cars  # Обновляем previous_dodged_cars


# --- Класс игрока ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw_image = pygame.image.load(os.path.join(os.path.expanduser("~"), 'Desktop', "Player.png"))
        self.image = pygame.transform.scale(raw_image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

    def move(self):
        """Обрабатывает движение игрока с клавишами влево и вправо."""
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.rect.left > ROAD_LEFT:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right < ROAD_RIGHT:
            self.rect.move_ip(5, 0)


# --- Класс монеты ---
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw_image = pygame.image.load(os.path.join(os.path.expanduser("~"), 'Desktop', "Coin.png"))
        self.image = pygame.transform.scale(raw_image, (40, 40))  # Размер монеты
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        """Создаёт монету сверху в случайной горизонтальной позиции."""
        self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), -50)

    def move(self):
        """Монета падает вниз."""
        self.rect.move_ip(0, SPEED // 2)  # Падает медленнее врага
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()  # Если вышла за экран, появляется сверху

    def draw(self, surface):
        surface.blit(self.image, self.rect)



# --- Создание объектов ---
P1 = Player()
E1 = Enemy()


# --- Группы спрайтов ---
enemies = pygame.sprite.Group()
enemies.add(E1)
C1 = Coin()

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# --- Ускорение со временем ---
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)

FramePerSec = pygame.time.Clock()
previous_dodged_cars = 0  # Чтобы отслеживать изменения
collected_coins = 0


def show_game_over():
    """Отображает улучшенный экран завершения игры с кнопками"""
    global dodged_cars, collected_coins

    DISPLAYSURF.fill((240, 240, 240))  # Светло-серый фон

    # Отображение "Game Over"
    game_over_text = pygame.font.Font(None, 64).render("Game Over", True, (30, 30, 30))
    DISPLAYSURF.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 180))

    # Отображение счета
    score_text = pygame.font.Font(None, 36).render(f"Dodged: {dodged_cars} | Coins: {collected_coins}", True, (50, 50, 50))
    DISPLAYSURF.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 260))

    # Создание кнопок
    button_width, button_height = 120, 50
    reset_button = pygame.Rect(SCREEN_WIDTH // 2 - button_width - 20, 350, button_width, button_height)
    quit_button = pygame.Rect(SCREEN_WIDTH // 2 + 20, 350, button_width, button_height)

    # Отрисовка кнопок с закругленными краями
    pygame.draw.rect(DISPLAYSURF, (34, 177, 76), reset_button, border_radius=12)  # Зеленая кнопка Reset
    pygame.draw.rect(DISPLAYSURF, (200, 50, 50), quit_button, border_radius=12)  # Красная кнопка Quit

    # Текст кнопок
    reset_text = pygame.font.Font(None, 32).render("Reset", True, (255, 255, 255))
    quit_text = pygame.font.Font(None, 32).render("Quit", True, (255, 255, 255))

    DISPLAYSURF.blit(reset_text, (reset_button.x + button_width // 4, reset_button.y + 10))
    DISPLAYSURF.blit(quit_text, (quit_button.x + button_width // 4, quit_button.y + 10))

    pygame.display.update()

    # Цикл ожидания кликов по кнопкам
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if reset_button.collidepoint(event.pos):
                    reset_game()  # Перезапуск
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()



def reset_game():
    pygame.quit()
    os.system("python " + __file__)  # Перезапуск кода
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT + 1:
            SPEED += 1  # Увеличиваем скорость на 1 каждую 2 секунды

    # --- Очистка экрана ---
    DISPLAYSURF.fill(WHITE)

    # --- Движение всех объектов ---
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # --- Проверка столкновения с врагами ---
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        time.sleep(0.5)
        show_game_over()

        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(game_over, (30, 250))

        # --- Отображение итогового счёта ---
        dodged_text = font_small.render(f"Dodged: {dodged_cars}", True, BLACK)
        coin_text = font_small.render(f"Coins: {collected_coins}", True, BLACK)


        DISPLAYSURF.blit(dodged_text, (150, 330))
        DISPLAYSURF.blit(coin_text, (170, 360))

        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # --- Проверка сбора монет ---
    if pygame.sprite.spritecollideany(P1, coins):
        collected_coins += 1
        for coin in coins:
            if pygame.sprite.collide_rect(P1, coin):
                coin.spawn()  # Создать новую монету

    # --- Увеличение SCORE только если dodged_cars изменился ---
    if dodged_cars > previous_dodged_cars:
        SCORE += 1
        previous_dodged_cars = dodged_cars

    # --- Отображение счёта в углу ---
    score_display = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_display = font_small.render(f"Coins: {collected_coins}", True, BLACK)

    DISPLAYSURF.blit(score_display, (10, 10))
    DISPLAYSURF.blit(coins_display, (SCREEN_WIDTH - 100, 10))  # В правом верхнем углу

    pygame.display.update()
    FramePerSec.tick(FPS)
