import pygame


def start_game():
    pygame.init()
    song = pygame.mixer.Sound(get_random_song())
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(20)
    pygame.quit()

def menu(num):
    result = 0
    if(num == 2):
        result == 1
    elif(num == 1):
        start_game()
        result == 0
    return result

print("Welcome to guess the melody game!\nChoose one of the options below!\n(1) - start the game, (2) - quit the game")
menu(input())