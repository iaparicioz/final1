import pygame
import sys
from pygame import *
import menuScreen

from connection import *

# pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("SERPIENCOVID GAME")
screen = pygame.display.set_mode([1000, 800])
fondo = pygame.image.load("images/fondoNegro2.jpg").convert()

base_font15 = pygame.font.Font("Snowy Night.ttf", 15)
base_font30 = pygame.font.Font("SF Hollywood Hills Italic.ttf", 30)
base_font40 = pygame.font.Font("SF Hollywood Hills.ttf", 40)
base_font50 = pygame.font.Font("Snowy Night.ttf", 50)
base_font65 = pygame.font.Font("Snowy Night.ttf", 65)
base_font75 = pygame.font.Font("Snowy Night.ttf", 75)
base_font100 = pygame.font.Font("SF Hollywood Hills.ttf", 100)

titleRanking = base_font100.render("RANKING", True, 'white')

back = Rect(50, 700, 200, 50)
textoBack = base_font75.render("BACK", True, 'white')

cursor = db.cursor()
cursor.execute("SELECT * FROM ranking ORDER BY points desc limit 3")
result = cursor.fetchall()

id1 = str(result[0][0])
textID1 = base_font30.render(id1, True, 'white')
nameUser1 = str(result[0][1])
textName1 = base_font30.render(nameUser1, True, 'white')
points1 = str(result[0][2])
textpoints1 = base_font30.render(points1, True, 'white')

id2 = str(result[1][0])
textID2 = base_font30.render(id2, True, 'white')
nameUser2 = str(result[1][1])
textName2 = base_font30.render(nameUser2, True, 'white')
points2 = str(result[1][2])
textpoints2 = base_font30.render(points2, True, 'white')

id3 = str(result[2][0])
textID3 = base_font30.render(id3, True, 'white')
nameUser3 = str(result[2][1])
textName3 = base_font30.render(nameUser3, True, 'white')
points3 = str(result[2][2])
textpoints3 = base_font30.render(points3, True, 'white')

titleId = base_font40.render("ID", True, 'white')
titleName = base_font40.render("NICKNAME", True, 'white')
titlePoints = base_font40.render("POINTS", True, 'white')

trofeo1 = pygame.image.load("images/trofeo1.png").convert_alpha()
trofeo2 = pygame.image.load("images/trofeo2.png").convert_alpha()
trofeo3 = pygame.image.load("images/trofeo3.png").convert_alpha()


def Ranking(user_text):
    # print(user_text)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ranking ORDER BY points desc limit 3")
    result = cursor.fetchall()

    id1 = str(result[0][0])
    textID1 = base_font30.render(id1, True, 'white')
    nameUser1 = str(result[0][1])
    textName1 = base_font30.render(nameUser1, True, 'white')
    points1 = str(result[0][2])
    textpoints1 = base_font30.render(points1, True, 'white')

    id2 = str(result[1][0])
    textID2 = base_font30.render(id2, True, 'white')
    nameUser2 = str(result[1][1])
    textName2 = base_font30.render(nameUser2, True, 'white')
    points2 = str(result[1][2])
    textpoints2 = base_font30.render(points2, True, 'white')

    id3 = str(result[2][0])
    textID3 = base_font30.render(id3, True, 'white')
    nameUser3 = str(result[2][1])
    textName3 = base_font30.render(nameUser3, True, 'white')
    points3 = str(result[2][2])
    textpoints3 = base_font30.render(points3, True, 'white')

    while True:
        screen.blit(fondo, [0, 0])
        screen.blit(titleRanking, (340, 155))

        screen.blit(titleId, (320, 320))
        screen.blit(textID1, (320, 410))
        screen.blit(textID2, (320, 470))
        screen.blit(textID3, (320, 530))

        lineSepar= base_font15.render("--------------------------------------------------------", True, 'white')
        screen.blit(lineSepar, (310, 360))

        screen.blit(titleName, (400, 320))
        screen.blit(textName1, (400, 410))
        screen.blit(textName2, (400, 470))
        screen.blit(textName3, (400, 530))

        screen.blit(titlePoints, (590, 320))
        screen.blit(textpoints1, (605, 410))
        screen.blit(textpoints2, (605, 470))
        screen.blit(textpoints3, (605, 530))

        screen.blit(trofeo1, (640, 400))
        screen.blit(trofeo2, (640, 460))
        screen.blit(trofeo3, (640, 520))

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
