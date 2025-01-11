import pygame
pygame.init()
pygame.mixer.music.load('ex010.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
