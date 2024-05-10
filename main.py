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

#Used To Slow Down The Launch Of Our Ship In def create_ship
VEL_SCALE = 100

#FPS The Window Runs At
FPS = 60

#Sets The Background To Our background.jpg Img And Scales It
BG = pygame.transform.scale(pygame.image.load('background.jpg'), (WIDTH, HEIGHT))

#Sets jupiter.png As The Planet We'll Use And Scales It
PLANET = pygame.transform.scale(pygame.image.load('jupiter.png'), (PLANET_SIZE * 2, PLANET_SIZE * 2))

#Colors Using RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#class Planet:
    
class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

#Handles The "Launching" Of Our Ship(Obj)
def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    obj = Spacecraft(t_x,t_y, vel_x, vel_y, SHIP_MASS)
    return obj

def main():
    running = True
    clock = pygame.time.Clock()
    objects = []
    temp_obj_pos = None

    while running:
        
        #Sets The FPS
        clock.tick(FPS)

        #Detects The Your Mouse's Position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Allows Us To Use MOUSEBUTTONDOWN To Aim Where We Launch The Ship(obj)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        #Puts Our Background Into The Loop
        win.blit(BG, (0, 0))

        if temp_obj_pos:

            #Draws A White Line To Show Us The Direction We're Launching Our Ship After Using MOUSEBUTTONDOWN
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos, 2)
            
            #Draws Our Ship(Obj) Just A Red Circle Rn
            pygame.draw.circle(win, RED, temp_obj_pos, OBJ_SIZE)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()