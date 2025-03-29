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
COINS_FOR_SPEED_INCREASE = 10  # Количество монет для увеличения скорости

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# --- Шрифты ---
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# --- Окно игры ---
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

crash_sound = pygame.mixer.Sound(os.path.join(os.path.expanduser("~"), 'Desktop', "crash.wav"))
# Функция загрузки изображения

def load_image(filename, default_size=(50, 50)):
    try:
        image = pygame.image.load(filename)
        return pygame.transform.scale(image, default_size)
    except pygame.error:
        print(f"Ошибка загрузки {filename}, используем заглушку")
        return pygame.Surface(default_size)  # Заглушка


# Загрузка звука
sound_path = os.path.join(os.path.expanduser("~"), 'Desktop', "crash.wav")
if os.path.exists(sound_path):
    crash_sound = pygame.mixer.Sound(sound_path)
else:
    crash_sound = None
    print("Звук crash.wav не найден")


# --- Классы объектов ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw_image = pygame.image.load(os.path.join(os.path.expanduser("~"), 'Desktop', "Player.png"))
        self.image = pygame.transform.scale(raw_image, (50, 100))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 120))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > ROAD_LEFT:
            self.rect.move_ip(-5, 0)
        if keys[K_RIGHT] and self.rect.right < ROAD_RIGHT:
            self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw_image = pygame.image.load(os.path.join(os.path.expanduser("~"), 'Desktop', "Enemy.png"))
        self.image = pygame.transform.scale(raw_image, (60, 100))
        self.rect = self.image.get_rect(center=(random.randint(ROAD_LEFT, ROAD_RIGHT), -100))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            global SCORE
            SCORE += 1
            self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), -100)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw_image = pygame.image.load(os.path.join(os.path.expanduser("~"), 'Desktop', "Coin.png"))
        self.base_image = pygame.transform.scale(raw_image, (40, 40))
        self.resize()
        self.rect = self.image.get_rect()
        self.spawn()

    def resize(self):
        """Изменяет размер монеты случайным образом."""
        self.size = random.randint(20, 60)  # Размер от 20 до 60 пикселей
        self.image = pygame.transform.scale(self.base_image, (self.size, self.size))

    def spawn(self):
        """Создаёт монету сверху в случайной горизонтальной позиции."""
        self.resize()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), -50)

    def move(self):
        """Монета падает вниз."""
        self.rect.move_ip(0, SPEED // 2)  # Падает медленнее врага
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()  # Если вышла за экран, появляется сверху


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

FramePerSec = pygame.time.Clock()
collected_coins = 0

def show_game_over():
    """Отображает улучшенный экран завершения игры с кнопками"""
    global dodged_cars, collected_coins

    DISPLAYSURF.fill((240, 240, 240))  # Светло-серый фон

    # Отображение "Game Over"
    game_over_text = pygame.font.Font(None, 64).render("Game Over", True, (30, 30, 30))
    DISPLAYSURF.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 180))

    # Отображение счета
    score_text = pygame.font.Font(None, 36).render(f" Coins: {collected_coins}", True, (50, 50, 50))
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

    # --- Проверка столкновения с врагом ---
    if pygame.sprite.spritecollideany(P1, enemies):
        crash_sound.play()
        time.sleep(0.5)
        show_game_over()

    # --- Проверка сбора монет ---
    collided_coins = pygame.sprite.spritecollide(P1, coins, True)  # Удаляет собранные монеты
    for coin in collided_coins:
        if coin.size >= 50:
            collected_coins += 3  # Большая монета - 3 очка
        else:
            collected_coins += 1  # Маленькая монета - 1 очко

        if collected_coins % COINS_FOR_SPEED_INCREASE == 0:
            SPEED += 1  # Увеличиваем скорость врагов при сборе N монет

        new_coin = Coin()  # Создаём новую монету
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # --- Отображение счёта в углу ---
    score_display = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins_display = font_small.render(f"Coins: {collected_coins}", True, BLACK)

    DISPLAYSURF.blit(score_display, (10, 10))
    DISPLAYSURF.blit(coins_display, (SCREEN_WIDTH - 100, 10))  # В правом верхнем углу

    pygame.display.update()
    FramePerSec.tick(FPS)
