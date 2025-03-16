import pygame
import os
import datetime

pygame.init()
HEIGHT,WIDTH = 800,800
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption('mickey clock')

desktop_path1 = os.path.join(os.path.expanduser('~'),'Desktop','clock.png')
desktop_path2 = os.path.join(os.path.expanduser('~'),'Desktop', 'min_hand.png')
desktop_path3 = os.path.join(os.path.expanduser('~'),'Desktop', 'sec_hand.png')

try:
    base = pygame.image.load(desktop_path1)
    minutesh = pygame.image.load(desktop_path2)
    secondh = pygame.image.load(desktop_path3)
except:
    print('could not load images')
    exit()

def draw_hand(image,angle,pivot,correction = 0):
    rotated_image = pygame.transform.rotate(image,angle+correction)
    new_rect = rotated_image.get_rect(center = pivot)
    screen.blit(rotated_image,new_rect)

center = (HEIGHT // 2, WIDTH // 2)
base_rect = base.get_rect(center = center)
minute_correction = - 47
second_correction = + 60

running = True
while running:
    screen.fill((255,255,255))
    screen.blit(base,base_rect.topleft)

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    seconds_angle = -(seconds * 6)
    minutes_angle = -(minutes * 6 + seconds * 0.1)

    draw_hand(minutesh,minutes_angle,center,minute_correction)
    draw_hand(secondh,seconds_angle,center,second_correction)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(100)

pygame.quit()

