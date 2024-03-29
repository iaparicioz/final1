import menuScreen
import pygame
from pygame import *
import sys
from connection import *


pygame.init()

# inicio de la pantalla

clock = pygame.time.Clock()
pygame.display.set_caption("SERPIENCOVID GAME")
screen = pygame.display.set_mode([1000, 800])

# letras para la pantalla
base_font15 = pygame.font.Font("Snowy Night.ttf", 15)
base_font30 = pygame.font.Font("SF Hollywood Hills.ttf", 30)
base_font40 = pygame.font.Font("SF Hollywood Hills.ttf", 40)
base_font50 = pygame.font.Font("SF Hollywood Hills.ttf", 50)
base_font65 = pygame.font.Font("SF Hollywood Hills.ttf", 65)
base_font75 = pygame.font.Font("SF Hollywood Hills.ttf", 75)
base_font100 = pygame.font.Font("SF Hollywood Hills.ttf", 100)
italic_font40 = pygame.font.Font("SF Hollywood Hills Italic.ttf", 40)

fondo = pygame.image.load("images/fondoNegro2.jpg").convert()

# colores para el cuadro del nickname y tamaño.
input_rect = pygame.Rect(350, 430, 85, 50)
color_active = pygame.Color('white')
color_passive = pygame.Color(215, 233, 212)
color = color_passive

# tamaño del cuadro de continuar
continue1 = Rect(380, 540, 250, 50)

textWelc = base_font100.render("SERPIENCOVID", True, 'white')
textSelect = base_font50.render("NICKNAME", True, 'white')

textFaltaUser = base_font50.render("INTRODUCE UNSFJKNFKW", True, 'white')


class MainRun:
    def __init__(self):
        self.run()

    @staticmethod
    def run():
        cursor = db.cursor()
        active = False
        user_text = ''
        # cambio = False
        while True:
            # screen.fill((255, 255, 255))
            screen.blit(fondo, [0, 0])
            screen.blit(textWelc, (250, 200))
            screen.blit(textSelect, (350, 370))
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(ev.pos):
                        active = True
                    else:
                        active = False

                if ev.type == pygame.KEYDOWN:
                    # para poder escribir el user_name

                    if active:
                        if ev.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += ev.unicode

                if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
                    if continue1.collidepoint(mouse.get_pos()):
                        if user_text != '':
                            try:
                                insertNickname = "INSERT INTO usuario (nameUser) VALUES ('" + user_text + "')"
                                cursor.execute(insertNickname)
                                db.commit()

                                insertRanking = """INSERT INTO ranking (nameUser, points) VALUES (%s, %s)"""
                                val = (user_text, 0)
                                cursor.execute(insertRanking, val)
                                db.commit()
                                cursor.close()
                                menuScreen.Menu(user_text)

                            except:
                                rojo = (212, 63, 53)
                                draw.rect(screen, rojo, input_rect)
                        
                        else:
                            # INTENTAR HACER QUE SI SE PONE ROJO CUANDO NO METO NOMBRE
                            # print("Introduce nickname :)")

                            # screen.blit(textFaltaUser, (30, 130))
                            # pygame.time.wait(5000)
                            # print("Nombre de usuario: ", user_text)
                            pygame.draw.rect(screen, (212, 63, 53), input_rect)


            # cambio de colores al pulsar el boton de continuar
            if continue1.collidepoint(mouse.get_pos()):
                draw.rect(screen, (177, 221, 170), continue1, 0)
            else:
                draw.rect(screen, (140, 176, 134), continue1, 0)

            if active:
                color = color_active
            else:
                color = color_passive

            pygame.draw.rect(screen, color, input_rect)
            # color de la letra
            text_surface = base_font40.render(user_text, True, (0, 0, 0))
            screen.blit(text_surface, (input_rect.x + 20, input_rect.y + 10))

            input_rect.w = max(300, text_surface.get_width() + 10)

            texto = italic_font40.render("CONTINUE", True, 'white')
            screen.blit(texto, (continue1.x + (continue1.width - texto.get_width()) / 2,
                    continue1.y + (continue1.height - texto.get_height()) / 2))

            display.flip()

            pygame.display.flip()
            clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    MainRun()
