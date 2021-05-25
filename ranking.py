import pygame
import sys
from pygame import *
import menuScreen

#pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SERPIENCOVID GAME")
screen = pygame.display.set_mode([1000, 800])
fondo = pygame.image.load("images/fondoNegro2.jpg").convert()

base_font15 = pygame.font.Font("Snowy Night.ttf", 15)
base_font30 = pygame.font.Font("Snowy Night.ttf", 30)
base_font40 = pygame.font.Font("Snowy Night.ttf", 40)
base_font50 = pygame.font.Font("Snowy Night.ttf", 50)
base_font65 = pygame.font.Font("Snowy Night.ttf", 65)
base_font75 = pygame.font.Font("Snowy Night.ttf", 75)
base_font100 = pygame.font.Font("Snowy Night.ttf", 100)

titleRanking = base_font100.render("RANKING", True, 'white')

back = Rect(50, 700, 200, 50)
textoBack = base_font75.render("BACK", True, 'white')


def Ranking(user_text):
    print(user_text)
    while True:
        screen.fill((144, 166, 108))
        screen.blit(titleRanking, (355, 100))
        screen.blit(fondo, [0, 0])
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if back.collidepoint(mouse.get_pos()):
                    menuScreen.Menu(user_text)

        pygame.draw.rect(screen, (0, 0, 0), back, 1)
        screen.blit(textoBack, (back.x + (back.width - textoBack.get_width()) / 2,
                                back.y + (back.height - textoBack.get_height()) / 2))
        pygame.display.flip()
        clock.tick(60)
