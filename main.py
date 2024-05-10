import pygame
import math

pygame.init()

#Sets The Width, Height, And Name Of The Window
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gravitational Slingshot')

#Mass Of The Planet And Ship(Obj) As Well As The Gravity. Affects The Slingshot Effect
PLANET_MASS = 100
SHIP_MASS = 5
G = 5

#Size Of The Planet And Our Ship(Obj)
PLANET_SIZE = 50
OBJ_SIZE = 5

VEL_SCALE = 100

#FPS The Window Runs At
FPS = 60

#Sets The Background To Our background.jpg Img And Scales It
BG = pygame.transform.scale(pygame.image.load('background.jpg'), (WIDTH, HEIGHT))

#Sets jupiter.png As The Planet We'll Use And Scales It
PLANET = pygame.transform.scale(pygame.image.load('jupiter.png'), (PLANET_SIZE * 2, PLANET_SIZE * 2))