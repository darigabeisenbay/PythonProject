import pygame
import random
import psycopg2
import sys
from config import host, user, password, db_name  # подключи свои данные

def connect_db():
    return psycopg2.connect(host=host, user=user, password=password, database=db_name)

def create_tables(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE NOT NULL
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
            level INTEGER,
            score INTEGER
        );
        """)
    connection.commit()

def get_or_create_user(connection, name):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM users WHERE name = %s", (name,))
        result = cursor.fetchone()
        if result:
            user_id = result[0]
        else:
            cursor.execute("INSERT INTO users (name) VALUES (%s) RETURNING id", (name,))
            user_id = cursor.fetchone()[0]
            connection.commit()

        cursor.execute("SELECT level, score FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
        score_data = cursor.fetchone()
        if score_data:
            return user_id, score_data[0], score_data[1]
        else:
            return user_id, 1, 0

def save_game(connection, user_id, level, score):
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)",
            (user_id, level, score)
        )
    connection.commit()
    print("Игра сохранена!")

# ------------------------- ИГРА -------------------------

class SnakeGame:
    def __init__(self, user_id, start_level=1, start_score=0):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/keeen/PycharmProjects/PythonProject/songz/blue.mp3")
        pygame.mixer.music.play(-1)

        self.WIDTH, self.HEIGHT = 600, 400
        self.WHITE, self.GREEN, self.RED, self.BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)
        self.FONT = pygame.font.Font(None, 30)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()

        self.snake_pos = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"
        self.food_pos = [random.randint(0, self.WIDTH // 10 - 1) * 10,
                         random.randint(0, self.HEIGHT // 10 - 1) * 10]

        self.score = start_score
        self.level = start_level
        self.speed = 10 + (self.level - 1) * 2
        self.running = True
        self.paused = False

        self.user_id = user_id

    def move_snake(self):
        if self.direction == "UP":
            self.snake_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_pos[1] += 10
        elif self.direction == "LEFT":
            self.snake_pos[0] -= 10
        elif self.direction == "RIGHT":
            self.snake_pos[0] += 10

        self.snake_body.insert(0, list(self.snake_pos))

        if self.snake_pos == self.food_pos:
            self.score += 1
            if self.score % 4 == 0:
                self.level += 1
                self.speed += 2
            self.food_pos = [random.randint(0, self.WIDTH // 10 - 1) * 10,
                             random.randint(0, self.HEIGHT // 10 - 1) * 10]
        else:
            self.snake_body.pop()

    def check_collision(self):
        if self.snake_pos[0] < 0 or self.snake_pos[0] >= self.WIDTH or \
           self.snake_pos[1] < 0 or self.snake_pos[1] >= self.HEIGHT or \
           self.snake_pos in self.snake_body[1:]:
            self.running = False

    def draw_elements(self):
        self.screen.fill(self.BLACK)
        for part in self.snake_body:
            pygame.draw.rect(self.screen, self.GREEN, pygame.Rect(part[0], part[1], 10, 10))
        pygame.draw.rect(self.screen, self.RED, pygame.Rect(self.food_pos[0], self.food_pos[1], 10, 10))
        score_text = self.FONT.render(f"Score: {self.score} | Level: {self.level}", True, self.WHITE)
        self.screen.blit(score_text, (20, 20))
        pygame.display.update()

    def pause_screen(self):
        pause_text = self.FONT.render("Пауза. Нажмите P чтобы продолжить", True, self.WHITE)
        self.screen.blit(pause_text, (self.WIDTH // 5, self.HEIGHT // 2))
        pygame.display.update()

    def game_over(self):
        self.screen.fill(self.BLACK)
        over = self.FONT.render(f"Game Over | Score: {self.score} | Level: {self.level}", True, self.WHITE)
        self.screen.blit(over, (self.WIDTH // 4, self.HEIGHT // 2))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def run(self, connection):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_game(connection, self.user_id, self.level, self.score)
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != "DOWN":
                        self.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.direction != "UP":
                        self.direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                        self.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                        self.direction = "RIGHT"
                    elif event.key == pygame.K_p:
                        self.paused = not self.paused
                        if self.paused:
                            self.pause_screen()
                    elif event.key == pygame.K_s:
                        save_game(connection, self.user_id, self.level, self.score)

            if not self.paused:
                self.move_snake()
                self.check_collision()
                self.draw_elements()
                self.clock.tick(self.speed)

        save_game(connection, self.user_id, self.level, self.score)
        self.game_over()


# --------- ЗАПУСК ---------
if __name__ == "__main__":
    conn = connect_db()
    create_tables(conn)
    name = input("Введите ваше имя: ")
    user_id, level, score = get_or_create_user(conn, name)
    print(f"Добро пожаловать, {name}! Ваш уровень: {level}, Очки: {score}")
    game = SnakeGame(user_id, level, score)
    game.run(conn)
