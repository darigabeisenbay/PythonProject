import pygame
import os

pygame.init()
HEIGHT,WIDTH = 400,300
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('songz🎶')

WHITE = (255,255,255)
music_folder = os.path.join(os.path.expanduser('~'), 'Desktop', 'songz')
tracks = [f for f in os.listdir(music_folder) if os.path.splitext(f)[1].lower() == '.mp3']
current_track_index = 0

def play_music(index):
    if 0 <= index < len(tracks):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(music_folder, tracks[index]))
        pygame.mixer.music.play()
        print(f"current song:{tracks[index]}")
    else:
        print("mistake occured")

play_music(current_track_index)
running = True
paused = False

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:
                current_track_index = (current_track_index + 1) % len(tracks)
                play_music(current_track_index)
            elif event.key == pygame.K_LEFT:
                current_track_index = (current_track_index - 1) % len(tracks)
                play_music(current_track_index)

    pygame.display.flip()
pygame.quit()
