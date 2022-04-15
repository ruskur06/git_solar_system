import pygame
from pygame.draw import *
from math import *

pygame.init()
FPS = 60
H = 740
W = 1000
r = 5

screen = pygame.display.set_mode((W, H))
x0, y0 = 500, 370 # solar
x1, y1 = 500, 470 # z
x2, y2 = 500, 410 # merc
x3, y3 = 500, 440 # venus
x4, y4 = 500, 500 # mars
x5, y5 = 500, 570 # jupiter
x6, y6 = 500, 630 #saturn
x7, y7 = 500, 680 #uran
x8, y8 = 500, 710 #neptun
R = y1 - y0 # z
R1 = y2 - y0 # merc
R2 = y3 - y0 # venus
R3 = y4 - y0 # mars
R4 = y5 - y0 # jupiter
R5 = y6 - y0 #saturn
R6 = y7 - y0 #uran
R7 = y8 - y0 #neptun
phi = 0
phon = pygame.image.load('phon.png')
new_phon = pygame.transform.scale(phon, (1000, 740))

def solar():
    sol = pygame.image.load('sol.png')
    new_sol = pygame.transform.scale(sol, (50, 50))
    screen.blit(new_sol, (x0 - 25, y0 - 25))
def star_tod():
    star_tod = pygame.image.load('star_tod.png')
    new_star_tod = pygame.transform.scale(star_tod, (50, 50))
    screen.blit(new_star_tod, (100, 100))
def z():
    zem = pygame.image.load('zem.png')
    new_z = pygame.transform.scale(zem, (10, 10))
    screen.blit(new_z, (x1, y1))
def merc():
    merc = pygame.image.load('merc.png')
    new_merc = pygame.transform.scale(merc, (5, 5))
    screen.blit(new_merc, (x2, y2))
def venus():
    venus = pygame.image.load('venus.png')
    new_z = pygame.transform.scale(venus, (10, 10))
    screen.blit(new_z, (x3, y3))
def mars():
    mars = pygame.image.load('mars.png')
    new_mars = pygame.transform.scale(mars, (8, 8))
    screen.blit(new_mars, (x4, y4))
def jupiter():
    jupiter = pygame.image.load('jupiter.png')
    new_jupiter = pygame.transform.scale(jupiter, (12.5, 12.5))
    screen.blit(new_jupiter, (x5, y5))
def saturn():
    saturn = pygame.image.load('saturn.png')
    new_saturn = pygame.transform.scale(saturn, (25, 10))
    screen.blit(new_saturn, (x6, y6))
def uran():
    uran = pygame.image.load('uran.png')
    new_uran = pygame.transform.scale(uran, (17, 30))
    screen.blit(new_uran,(x7, y7))
def neptun():
    neptun = pygame.image.load('neptun.png')
    new_neptun = pygame.transform.scale(neptun, (25, 25))
    screen.blit(new_neptun, (x8, y8))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


    solar()
    star_tod()
    merc()
    venus()
    z()
    mars()
    jupiter()
    saturn()
    uran()
    neptun()
    x1 = x0 + R * (cos(phi))
    y1 = y0 - R * (sin(phi))
    x2 = x0 + R1 * (cos(phi*2))
    y2 = y0 - R1 * (sin(phi*2))
    x3 = x0 + R2 * (cos(phi * 1.5))
    y3 = y0 - R2 * (sin(phi * 1.5))
    x4 = x0 + R3 * (cos(phi * 0.9))
    y4 = y0 - R3 * (sin(phi * 0.9))
    x5 = x0 + R4 * (cos(phi * 0.75))
    y5 = y0 - R4 * (sin(phi * 0.75))
    x6 = x0 + R5 * (cos(phi * 0.6))
    y6 = y0 - R5 * (sin(phi * 0.6))
    x7 = x0 + R6 * (cos(phi * 0.4))
    y7 = y0 - R6 * (sin(phi * 0.4))
    x8 = x0 + R7 * (cos(phi * 0.2))
    y8 = y0 - R7 * (sin(phi * 0.2))

    phi += 0.05
    pygame.display.update()
    screen.blit(new_phon, (0, 0))


pygame.quit()