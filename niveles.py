import sys
from pygame import *
from juego import *

import menuScreen

#pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SERPIENCOVID GAME")
screen = pygame.display.set_mode([1000, 800])
fondo = pygame.image.load("images/fondoNegro2.jpg").convert()

nivel1 = Rect(320, 340, 150, 50)
nivel2 = Rect(320, 500, 150, 50)
nivel3 = Rect(320, 550, 150, 50)
nivel4 = Rect(520, 340, 150, 50)
nivel5 = Rect(520, 500, 150, 50)
nivel6 = Rect(520, 550, 150, 50)


base_font15 = pygame.font.Font("Snowy Night.ttf", 15)
base_font25 = pygame.font.Font("SF Hollywood Hills.ttf", 25)
base_font30 = pygame.font.Font("SF Hollywood Hills.ttf", 30)
base_font40 = pygame.font.Font("SF Hollywood Hills.ttf", 40)
base_font50 = pygame.font.Font("Snowy Night.ttf", 50)
base_font65 = pygame.font.Font("Snowy Night.ttf", 65)
base_font75 = pygame.font.Font("SF Hollywood Hills.ttf", 75)
base_font100 = pygame.font.Font("SF Hollywood Hills.ttf", 100)
italic_font40 = pygame.font.Font("SF Hollywood Hills Italic.ttf", 40)


titleNivel = base_font100.render("LEVELS", True, 'white')
textoNivel1 = italic_font40.render("LEVEL 1", True, 'white')
textoNivel2 = italic_font40.render("LEVEL 2", True, 'white')
textoNivel3 = italic_font40.render("LEVEL 3", True, 'white')
textoNivel4 = italic_font40.render("LEVEL 4", True, 'white')
textoNivel5 = italic_font40.render("LEVEL 5", True, 'white')
textoNivel6 = italic_font40.render("LEVEL 6", True, 'white')

textoCovid = base_font25.render("¿COVID-19...?", True, (140, 176, 134))
textoConf = base_font25.render(" LOCKDOWN", True, (140, 176, 134))
textoRest = base_font25.render("RESTRICTIONS", True, (140, 176, 134))
textoBye = base_font25.render("BYE EMERGENCY STATE", True, (140, 176, 134))

back = Rect(50, 700, 200, 50)
textoBack = base_font75.render("BACK", True, (255, 255, 255))


snake = Snake


def Niveles(user_text):
    # print(user_text)
    while True:
        screen.blit(fondo, [0, 0])
        screen.blit(titleNivel, (370, 150))
        screen.blit(textoCovid, (310, 300))
        screen.blit(textoConf, (310, 450))
        screen.blit(textoRest, (520, 300))
        screen.blit(textoBye, (520, 450))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if nivel1.collidepoint(mouse.get_pos()):
                    # print("Hola 1")
                    game = Game(user_text, "fondoAzul1.jpg", "murcielago-3.png", "pangolin1-2.png", "kiss-2.png", "snakeojos.jpg")
                    game.reset()
                    game.run(tiempo=0.40)
                elif nivel2.collidepoint(mouse.get_pos()):
                    # print("Hola 2")
                    game = Game(user_text, "casaoscura.jpg", "papelhigienico-2.png", "gelh-2.png", "avioncito-2.png", "snakeojos.jpg")
                    game.reset()
                    game.run(tiempo=0.30)
                elif nivel3.collidepoint(mouse.get_pos()):
                    # print("Hola 3")
                    game = Game(user_text, "cocinaoscura.jpg", "teams-2.png", "harina-2.png", "party40-2.png", "snakeojosmask.jpg")
                    game.reset()
                    game.run(tiempo=0.25)
                elif nivel4.collidepoint(mouse.get_pos()):
                    # print("Hola 4")
                    game = Game(user_text, "campo4byn.jpg", "bici-2.png", "mascarilla-2.png", "kiss-2.png", "snakeojosmask.jpg")
                    game.reset()
                    game.run(tiempo=0.20)
                elif nivel5.collidepoint(mouse.get_pos()):
                    # print("Hola 5")
                    game = Game(user_text, "puertasolbyn2.jpg", "cerveza-2.png", "copita-2.png", "avioncito-2.png", "snakeojos.jpg")
                    game.reset()
                    game.run(tiempo=0.15)
                elif nivel6.collidepoint(mouse.get_pos()):
                    # print("Hola 6")
                    game = Game(user_text, "covid6.jpg", "vacun-2.png", "pill-3.png", "party40-2.png", "snakeojosmask.jpg")
                    game.reset()
                    game.run(tiempo=0.10)
                elif back.collidepoint(mouse.get_pos()):
                    menuScreen.Menu(user_text)

        pygame.draw.rect(screen, (0, 0, 0), nivel1, 0)
        screen.blit(textoNivel1, (nivel1.x + (nivel1.width - textoNivel1.get_width()) / 2,
                                  nivel1.y + (nivel1.height - textoNivel1.get_height()) / 2))

        pygame.draw.rect(screen, (0, 0, 0), nivel2, 0)
        screen.blit(textoNivel2, (nivel2.x + (nivel2.width - textoNivel2.get_width()) / 2,
                                  nivel2.y + (nivel2.height - textoNivel2.get_height()) / 2))

        pygame.draw.rect(screen, (0, 0, 0), nivel3, 0)
        screen.blit(textoNivel3, (nivel3.x + (nivel3.width - textoNivel3.get_width()) / 2,
                                  nivel3.y + (nivel3.height - textoNivel3.get_height()) / 2))

        pygame.draw.rect(screen, (0, 0, 0), nivel4, 0)
        screen.blit(textoNivel4, (nivel4.x + (nivel4.width - textoNivel4.get_width()) / 2,
                                  nivel4.y + (nivel4.height - textoNivel4.get_height()) / 2))

        pygame.draw.rect(screen, (0, 0, 0), nivel5, 0)
        screen.blit(textoNivel5, (nivel5.x + (nivel5.width - textoNivel5.get_width()) / 2,
                                  nivel5.y + (nivel5.height - textoNivel5.get_height()) / 2))

        pygame.draw.rect(screen, (0, 0, 0), nivel6, 0)
        screen.blit(textoNivel6, (nivel6.x + (nivel6.width - textoNivel6.get_width()) / 2,
                                  nivel6.y + (nivel6.height - textoNivel6.get_height()) / 2))

        pygame.draw.rect(screen, (0, 0, 0), back, 1)
        screen.blit(textoBack, (back.x + (back.width - textoBack.get_width()) / 2,
                                back.y + (back.height - textoBack.get_height()) / 2))

        pygame.display.flip()
        clock.tick(60)
