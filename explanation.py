import pygame
from pygame import *
import sys

import menuScreen

#pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SERPIENCOVID GAME")
screen = pygame.display.set_mode([1000, 800])
# letras para la pantalla
base_font15 = pygame.font.Font("Snowy Night.ttf", 15)
base_font30 = pygame.font.Font("SF Hollywood Hills Italic.ttf", 30)
base_font40 = pygame.font.Font("Snowy Night.ttf", 40)
base_font50 = pygame.font.Font("Snowy Night.ttf", 50)
base_font65 = pygame.font.Font("Snowy Night.ttf", 65)
base_font75 = pygame.font.Font("SF Hollywood Hills.ttf", 75)
base_font100 = pygame.font.Font("Snowy Night.ttf", 100)

back = Rect(50, 700, 200, 50)
textoBack = base_font75.render("BACK", True, (255, 255, 255))
texto1 = base_font30.render("Explicacion", True, 'white')

fondo = pygame.image.load("images/fondoNegro2.jpg").convert()


def Explanation(user_text):
    print(user_text)
    while True:
        # screen.fill((255, 255, 255))
        screen.blit(fondo, [0, 0])
        screen.blit(texto1, (250, 400))
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if eve.type == MOUSEBUTTONDOWN and eve.button == 1:
                if back.collidepoint(mouse.get_pos()):
                    menuScreen.Menu(user_text)

        pygame.draw.rect(screen, (89, 121, 80), back, 1)
        screen.blit(textoBack, (back.x + (back.width - textoBack.get_width()) / 2,
                                back.y + (back.height - textoBack.get_height()) / 2))

        pygame.display.flip()
        clock.tick(60)
