import pygame
import sys
from pygame import *
import menuScreen

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SERPIENCOVID GAME")
screen = pygame.display.set_mode([1000, 800])
fondo = pygame.image.load("images/fondoBueno.jpg").convert()

base_font15 = pygame.font.Font("Snowy Night.ttf", 15)
base_font30 = pygame.font.Font("Snowy Night.ttf", 30)
base_font40 = pygame.font.Font("Snowy Night.ttf", 40)
base_font50 = pygame.font.Font("Snowy Night.ttf", 50)
base_font65 = pygame.font.Font("Snowy Night.ttf", 65)
base_font75 = pygame.font.Font("Snowy Night.ttf", 75)
base_font100 = pygame.font.Font("Snowy Night.ttf", 100)

titleCredits = base_font100.render("CREDITS", True, (255, 255, 255))
textoMade = base_font40.render("MADE BY IVONNE APARICIO :)", True, (255, 255, 255))
textoTh = base_font40.render("THANKS FOR PLAYING", True, (255, 255, 255))


back = Rect(50, 700, 200, 50)
textoBack = base_font75.render("BACK", True, (255, 255, 255))


def Credits(user_text):
    print(user_text)
    while True:
        screen.blit(fondo, [0, 0])
        screen.blit(titleCredits, (350, 155))
        screen.blit(textoMade, (300, 325))
        screen.blit(textoTh, (350, 375))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if back.collidepoint(mouse.get_pos()):
                    menuScreen.Menu(user_text)

        pygame.draw.rect(screen, (89, 121, 80), back, 1)
        screen.blit(textoBack, (back.x + (back.width - textoBack.get_width()) / 2,
                                back.y + (back.height - textoBack.get_height()) / 2))
        pygame.display.flip()
        clock.tick(60)
