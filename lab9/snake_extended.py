import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load(os.path.join(os.path.expanduser("~"), 'Desktop', 'blue.mp3'))
pygame.mixer.music.play(-1)

# Константы для окна и цветов
WIDTH, HEIGHT = 600, 400
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)
FONT = pygame.font.Font(None, 30)

# Инициализация экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


class SnakeGame:
    def __init__(self):
        """Инициализация параметров игры"""
        self.snake_pos = [100, 50]  # Начальная позиция змейки
        self.snake_body = [[100, 50], [90, 50], [80, 50]]  # Тело змейки
        self.direction = "RIGHT"  # Начальное направление движения
        self.food_spawn_time = pygame.time.get_ticks()

        self.spawn_food()

        self.score = 0  # Очки
        self.level = 1  # Уровень
        self.speed = 10  # Начальная скорость змейки
        self.running = True  # Флаг работы игры

    def spawn_food(self):
        """Создание новой еды с разным весом"""
        self.food_pos = [random.randint(0, WIDTH // 10 - 1) * 10, random.randint(0, HEIGHT // 10 - 1) * 10]
        self.food_value = random.choice([1, 2, 3])  # Вес еды (очки)
        self.food_spawn_time = pygame.time.get_ticks()

    def move_snake(self):
        """Обновление позиции змейки"""
        if self.direction == "UP":
            self.snake_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_pos[1] += 10
        elif self.direction == "LEFT":
            self.snake_pos[0] -= 10
        elif self.direction == "RIGHT":
            self.snake_pos[0] += 10

        self.snake_body.insert(0, list(self.snake_pos))  # Добавляем новую голову змейки

        # Проверяем, съела ли змейка еду
        if self.snake_pos == self.food_pos:
            self.score += self.food_value

            # Повышение уровня каждые 4 очка
            if self.score % 4 == 0:
                self.level += 1
                self.speed += 2

            # Генерация новой еды
            self.spawn_food()
        else:
            self.snake_body.pop()  # Убираем последний сегмент змейки, если еда не съедена

        # Проверка времени жизни еды
        if pygame.time.get_ticks() - self.food_spawn_time > 5000:  # 5 секунд
            self.spawn_food()

    def check_collision(self):
        """Проверка столкновений"""
        # Столкновение со стенами
        if self.snake_pos[0] < 0 or self.snake_pos[0] >= WIDTH or self.snake_pos[1] < 0 or self.snake_pos[1] >= HEIGHT:
            self.running = False

        # Столкновение с самим собой
        if self.snake_pos in self.snake_body[1:]:
            self.running = False

    def draw_elements(self):
        """Отрисовка всех элементов на экране"""
        screen.fill(BLACK)

        # Отрисовка змейки
        for p in self.snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(p[0], p[1], 10, 10))

        # Отрисовка еды (размер зависит от веса)
        pygame.draw.rect(screen, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], 10 + self.food_value * 2,
                                                  10 + self.food_value * 2))

        # Отображение счета и уровня
        score_text = FONT.render(f"Score: {self.score} | Level: {self.level}", True, WHITE)
        screen.blit(score_text, (20, 20))

        pygame.display.update()

    def game_over(self):
        """Экран завершения игры"""
        screen.fill(BLACK)
        game_over_text = FONT.render(f"Game Over | Score: {self.score} | Level: {self.level}", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 2))
        pygame.display.update()

        # Оставляем экран открытым после окончания игры
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def run(self):
        """Основной игровой цикл"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Управление змейкой
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != "DOWN":
                        self.direction = "UP"
                    if event.key == pygame.K_DOWN and self.direction != "UP":
                        self.direction = "DOWN"
                    if event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    if event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.direction = "RIGHT"

            self.move_snake()
            self.check_collision()
            self.draw_elements()
            clock.tick(self.speed)  # Управление скоростью игры

        self.game_over()


# Запуск игры
if __name__ == "__main__":
    game = SnakeGame()
    game.run()
