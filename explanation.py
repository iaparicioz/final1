import pygame
from pygame import *
import sys

import menuScreen

# pygame.init()
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
texto1 = base_font15.render("The game I have created is an adaptation of the 'Snake' video game, ", True, 'white')
texto2 = base_font15.render("released in the mid-1970s set with the stages that we have gone ", True, 'white')
texto3 = base_font15.render("through the COVID-19 pandemic.", True, 'white')

texto4 = base_font15.render("In the game, the user or player controls a long and thin creature,", True, 'white')
texto5 = base_font15.render("similar to a snake that wanders around the screen which is a 2D plane, ", True, 'white')
texto6 = base_font15.render("picking up objects, trying to avoid hitting its tail or the 'walls' that ", True, 'white')
texto7 = base_font15.render("surround the game area.", True, 'white')

texto8 = base_font15.render("Every time the snake eats a 'positive' object (things, moments, or ", True, 'white')
texto9 = base_font15.render("objects that we have used or done depending on the stage of the pandemic),", True, 'white')
texto10 = base_font15.render("the tail grows longer, thus increasing the difficulty of the game. ", True, 'white')

texto11 = base_font15.render("And every time a 'negative' object is eaten (things, moments, or ", True, 'white')
texto12 = base_font15.render("objects that we could not use or do depending on the stage of the pandemic), ", True,
                             'white')
texto13 = base_font15.render("the game takes away the lives from the snake, which makes you have fewer ", True, 'white')
texto14 = base_font15.render("possibilities of winning.", True, 'white')

textoExp1 = base_font15.render("The user must control said snake using the up, down, right, or left keys ", True,
                               'white')
textoExp2 = base_font15.render("of the keyboard and while the game is running the snake will not stop.", True, 'white')

texto15 = base_font15.render("Examples of 'negative' objects: ", True, 'white')

fondo = pygame.image.load("images/fondoNegro2.jpg").convert()
bad1 = pygame.image.load("images/avioncito-2.png").convert_alpha()
bad2 = pygame.image.load("images/kiss-2.png").convert_alpha()
bad3 = pygame.image.load("images/party40-2.png").convert_alpha()


def Explanation(user_text):
    print(user_text)
    while True:
        # screen.fill((255, 255, 255))
        screen.blit(fondo, [0, 0])
        screen.blit(texto1, (250, 150))
        screen.blit(texto2, (250, 170))
        screen.blit(texto3, (250, 190))

        screen.blit(texto4, (250, 230))
        screen.blit(texto5, (250, 250))
        screen.blit(texto6, (250, 270))
        screen.blit(texto7, (250, 290))

        screen.blit(texto8, (250, 330))
        screen.blit(texto9, (250, 350))
        screen.blit(texto10, (250, 370))

        screen.blit(texto11, (250, 410))
        screen.blit(texto12, (250, 430))
        screen.blit(texto13, (250, 450))
        screen.blit(texto14, (250, 470))

        screen.blit(textoExp1, (250, 510))
        screen.blit(textoExp2, (250, 530))
        screen.blit(texto15, (250, 600))
        screen.blit(bad1, (500, 590))
        screen.blit(bad2, (550, 590))
        screen.blit(bad3, (600, 590))

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
