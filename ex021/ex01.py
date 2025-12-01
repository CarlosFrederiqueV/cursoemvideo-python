import pygame # type: ignore
pygame.init()
pygame.mixer.music.load('colocar o arquivo que deseja tocar')
pygame.mixer.music.play()
pygame.event.wait()