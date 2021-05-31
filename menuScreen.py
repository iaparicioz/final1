import sys
import pygame
from pygame import *

import credits
import niveles
import ranking
import explanation


#pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SERPIENCOVID GAME")
screen = pygame.display.set_mode([1000, 800])
fondo = pygame.image.load("images/fondoNegro2.jpg").convert()

base_font15 = pygame.font.Font("Snowy Night.ttf", 15)
base_font30 = pygame.font.Font("SF Hollywood Hills.ttf", 30)
base_font40 = pygame.font.Font("Snowy Night.ttf", 40)
base_font50 = pygame.font.Font("Snowy Night.ttf", 50)
base_font65 = pygame.font.Font("Snowy Night.ttf", 65)
base_font75 = pygame.font.Font("SF Hollywood Hills.ttf", 75)
base_font100 = pygame.font.Font("SF Hollywood Hills.ttf", 100)
italic_font30 = pygame.font.Font("SF Hollywood Hills Italic.ttf", 30)

menuTitle = base_font100.render("MAIN MENU", True, 'white')
textoStart = base_font75.render("START", True, 'white')
textoRanking = base_font75.render("RANKING", True, 'white')
textoCredits = base_font75.render("CREDITS", True, 'white')

startButton = Rect(375, 300, 250, 50)
rankingButton = Rect(375, 400, 250, 50)
creditsButton = Rect(375, 500, 250, 50)
whatAbout = Rect(310, 600, 400, 50)


def Menu(user_text):
    print(user_text)
    while True:
        screen.blit(fondo, [0, 0])
        screen.blit(menuTitle, (300, 150))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if startButton.collidepoint(mouse.get_pos()):
                    # print("Hola start")
                    niveles.Niveles(user_text)
                elif rankingButton.collidepoint(mouse.get_pos()):
                    # print("Hola ranking")
                    ranking.Ranking(user_text)
                elif creditsButton.collidepoint(mouse.get_pos()):
                    # print("Hola credits")
                    credits.Credits(user_text)
                elif whatAbout.collidepoint(mouse.get_pos()):
                    explanation.Explanation(user_text)

        if whatAbout.collidepoint(mouse.get_pos()):
            draw.rect(screen, (140, 176, 134), whatAbout, 0)
        else:
            draw.rect(screen, (0, 0, 0), whatAbout, 0)

        pygame.draw.rect(screen, (0, 0, 0), startButton, 0)
        screen.blit(textoStart, (startButton.x + (startButton.width - textoStart.get_width()) / 2,
                                 startButton.y + (startButton.height - textoStart.get_height()) / 2))

        pygame.draw.rect(screen, (0, 0, 0), rankingButton, 0)
        screen.blit(textoRanking, (rankingButton.x + (rankingButton.width - textoRanking.get_width()) / 2,
                                   rankingButton.y + (rankingButton.height - textoRanking.get_height()) / 2))

        pygame.draw.rect(screen, (0, 0, 0), creditsButton, 0)
        screen.blit(textoCredits, (creditsButton.x + (creditsButton.width - textoCredits.get_width()) / 2,
                                   creditsButton.y + (creditsButton.height - textoCredits.get_height()) / 2))

        texto2 = italic_font30.render("What is the game about?", True, 'white')
        screen.blit(texto2, (whatAbout.x + (whatAbout.width - texto2.get_width()) / 2,
                             whatAbout.y + (whatAbout.height - texto2.get_height()) / 2))

        pygame.display.flip()
        clock.tick(60)
