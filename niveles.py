import sys
from pygame import *
from juego import *

import menuScreen

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SERPIENCOVID GAME")
screen = pygame.display.set_mode([1000, 800])
fondo = pygame.image.load("images/fondoBueno.jpg").convert()

nivel1 = Rect(280, 350, 150, 50)
nivel2 = Rect(280, 500, 150, 50)
nivel3 = Rect(280, 550, 150, 50)
nivel4 = Rect(530, 350, 150, 50)
nivel5 = Rect(530, 500, 150, 50)
nivel6 = Rect(530, 550, 150, 50)


base_font15 = pygame.font.Font("Snowy Night.ttf", 15)
base_font30 = pygame.font.Font("Snowy Night.ttf", 30)
base_font40 = pygame.font.Font("Snowy Night.ttf", 40)
base_font50 = pygame.font.Font("Snowy Night.ttf", 50)
base_font65 = pygame.font.Font("Snowy Night.ttf", 65)
base_font75 = pygame.font.Font("Snowy Night.ttf", 75)
base_font100 = pygame.font.Font("Snowy Night.ttf", 100)


titleNivel = base_font100.render("LEVELS", True, 'white')
textoNivel1 = base_font40.render("LEVEL 1", True, (189, 224, 177))
textoNivel2 = base_font40.render("LEVEL 2", True, (189, 224, 177))
textoNivel3 = base_font40.render("LEVEL 3", True, (189, 224, 177))
textoNivel4 = base_font40.render("LEVEL 4", True, (189, 224, 177))
textoNivel5 = base_font40.render("LEVEL 5", True, (189, 224, 177))
textoNivel6 = base_font40.render("LEVEL 6", True, (189, 224, 177))

textoCovid = base_font30.render("¿COVID-19...?", True, 'white')
textoConf = base_font30.render(" LOCKDOWN", True, 'white')
textoRest = base_font30.render("RESTRICTIONS", True, 'white')
textoBye = base_font30.render("BYE STATE OF ALARM", True, 'white')

back = Rect(50, 700, 200, 50)
textoBack = base_font75.render("BACK", True, (255, 255, 255))


snake = Snake


def Niveles(user_text):
    print(user_text)
    while True:
        screen.blit(fondo, [0, 0])
        screen.blit(titleNivel, (375, 125))
        screen.blit(textoCovid, (270, 300))
        screen.blit(textoConf, (270, 450))
        screen.blit(textoRest, (520, 300))
        screen.blit(textoBye, (520, 450))

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button == 1:
                if nivel1.collidepoint(mouse.get_pos()):
                    # print("Hola 1")
                    game = Game("covid1byn.jpg", "murcielago.jpg", "pangolin-2.jpg", "hug1.jpg","snakeojos.jpg")
                    game.reset()
                    game.run(tiempo=0.40)
                elif nivel2.collidepoint(mouse.get_pos()):
                    # print("Hola 2")
                    game = Game("casa2byn.jpg", "papel2.jpg", "gel2.jpg","kiss2.jpg", "snakeojos.jpg")
                    game.reset()
                    game.run(tiempo=0.30)
                elif nivel3.collidepoint(mouse.get_pos()):
                    # print("Hola 3")
                    game = Game("cocina3byn.jpg", "teams3.jpg", "biscuit3.jpg","party3.jpg", "snakeojosmask.jpg")
                    game.reset()
                    game.run(tiempo=0.25)
                elif nivel4.collidepoint(mouse.get_pos()):
                    # print("Hola 4")
                    game = Game("campo4byn.jpg", "bici4.jpg", "PCR4.jpg", "hug4.jpg","snakeojosmask.jpg")
                    game.reset()
                    game.run(tiempo=0.20)
                elif nivel5.collidepoint(mouse.get_pos()):
                    # print("Hola 5")
                    game = Game("puertasolbyn2.jpg", "cerve5.jpg", "gin5.jpg","kiss5.jpg", "snakeojos.jpg")
                    game.reset()
                    game.run(tiempo=0.15)
                elif nivel6.collidepoint(mouse.get_pos()):
                    # print("Hola 6")
                    game = Game("covid6.jpg", "vacuna6.jpg", "pill6.jpg","party6.jpg", "snakeojosmask.jpg")
                    game.reset()
                    game.run(tiempo=0.10)
                elif back.collidepoint(mouse.get_pos()):
                    menuScreen.Menu(user_text)

        pygame.draw.rect(screen, (89, 121, 80), nivel1, 0)
        screen.blit(textoNivel1, (nivel1.x + (nivel1.width - textoNivel1.get_width()) / 2,
                                  nivel1.y + (nivel1.height - textoNivel1.get_height()) / 2))

        pygame.draw.rect(screen, (89, 121, 80), nivel2, 0)
        screen.blit(textoNivel2, (nivel2.x + (nivel2.width - textoNivel2.get_width()) / 2,
                                  nivel2.y + (nivel2.height - textoNivel2.get_height()) / 2))

        pygame.draw.rect(screen, (89, 121, 80), nivel3, 0)
        screen.blit(textoNivel3, (nivel3.x + (nivel3.width - textoNivel3.get_width()) / 2,
                                  nivel3.y + (nivel3.height - textoNivel3.get_height()) / 2))

        pygame.draw.rect(screen, (89, 121, 80), nivel4, 0)
        screen.blit(textoNivel4, (nivel4.x + (nivel4.width - textoNivel4.get_width()) / 2,
                                  nivel4.y + (nivel4.height - textoNivel4.get_height()) / 2))

        pygame.draw.rect(screen, (89, 121, 80), nivel5, 0)
        screen.blit(textoNivel5, (nivel5.x + (nivel5.width - textoNivel5.get_width()) / 2,
                                  nivel5.y + (nivel5.height - textoNivel5.get_height()) / 2))

        pygame.draw.rect(screen, (89, 121, 80), nivel6, 0)
        screen.blit(textoNivel6, (nivel6.x + (nivel6.width - textoNivel6.get_width()) / 2,
                                  nivel6.y + (nivel6.height - textoNivel6.get_height()) / 2))

        pygame.draw.rect(screen, (89, 121, 80), back, 1)
        screen.blit(textoBack, (back.x + (back.width - textoBack.get_width()) / 2,
                                back.y + (back.height - textoBack.get_height()) / 2))

        pygame.display.flip()
        clock.tick(60)
