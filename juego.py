import pygame
from pygame.locals import *
import time
import random

# objects y snake con 40px
SIZE = 40
#pygame.init()


class Object:
    def __init__(self, parent_screen, imagen, imagen2, bad):
        self.parent_screen = parent_screen
        self.image1 = pygame.image.load(f"images/{imagen}").convert_alpha()
        self.image2 = pygame.image.load(f"images/{imagen2}").convert_alpha()
        self.bad = pygame.image.load(f"images/{bad}").convert_alpha()

        # posicion de inicio del objeto 1
        self.x = SIZE * 4
        self.y = SIZE * 4

        # posicion de inicio del objeto 2
        self.x2 = SIZE * 14
        self.y2 = SIZE * 14

        # posicion de malo
        self.x3 = SIZE * 16
        self.y3 = SIZE * 16

    def draw(self):
        # pinto los objects en sus posiciones
        self.parent_screen.blit(self.image1, (self.x, self.y))
        self.parent_screen.blit(self.image2, (self.x2, self.y2))
        self.parent_screen.blit(self.bad, (self.x3, self.y3))
        pygame.display.flip()  # updating the screen

    def moveObject1(self):
        # ubicaciones donde queremos que se ubiquen los objects en aleatorio
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE

        self.x3 = random.randint(1, 24) * SIZE
        self.y3 = random.randint(1, 19) * SIZE

    def moveObject2(self):
        self.x2 = random.randint(1, 24) * SIZE
        self.y2 = random.randint(1, 19) * SIZE

        self.x3 = random.randint(1, 24) * SIZE
        self.y3 = random.randint(1, 19) * SIZE

    def moveObject3(self):
        self.x3 = random.randint(1, 24) * SIZE
        self.y3 = random.randint(1, 19) * SIZE


class Snake:

    def __init__(self, parent_screen, length, fondo, face):
        self.length = length
        self.parent_screen = parent_screen
        '''self.color1 = color1
        self.color2 = color2
        self.color3 = color3'''
        self.face = face

        self.fondo1 = pygame.image.load(f"images/{fondo}").convert()

        # imagenes de la serpiente, cuerpo y cola.
        self.block = pygame.image.load("images/snake40.jpg").convert()
        self.face1 = pygame.image.load(f"images/{face}").convert()
        # self.blockeyes = pygame.image.load("images/snakeojos.jpg").convert()
        # self.blockmask = pygame.image.load("images/snakeojosmask.jpg").convert()
        self.blockcola = pygame.image.load("images/cola5.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length

        self.direction = 'down'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    '''def reduce_length(self):
        self.length += 1
        self.x.pop(-1)
        self.y.pop(-1) '''

    def move_left(self):
        if self.direction != "right":
            self.direction = 'left'

    def move_right(self):
        if self.direction != "left":
            self.direction = 'right'

    def move_up(self):
        if self.direction != "down":
            self.direction = 'up'

    def move_down(self):
        if self.direction != "up":
            self.direction = 'down'

    def draw(self):
        self.parent_screen.blit(self.fondo1, (0, 0))
        self.parent_screen.blit(self.face1, (self.x[0], self.y[0]))
        # pintamos la sepriente
        for i in range(1, self.length - 1):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        # pintamos la cola.
        self.parent_screen.blit(self.blockcola, (self.x[-1], self.y[-1]))
        pygame.display.flip()  # updating the screen

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # coordenadas de pared, si llega se choca y gameover
        if self.direction == 'left':
            self.x[0] -= SIZE
            if self.x[0] < 0:
                Game.show_game_over()

        if self.direction == 'right':
            self.x[0] += SIZE
            if self.x[0] > 1000:
                Game.show_game_over()

        if self.direction == 'up':
            self.y[0] -= SIZE
            if self.y[0] < 0:
                Game.show_game_over()

        if self.direction == 'down':
            self.y[0] += SIZE
            if self.y[0] > 800:
                Game.show_game_over()

        self.draw()


class Game:
    def __init__(self, fondo1, imagen, imagen2, bad, face1):
        # print(n1)
        '''self.n1 = n1
        self.n2 = n2
        self.n3 = n3'''
        self.fondo1 = fondo1
        self.imagen = imagen
        self.imagen2 = imagen2
        self.bad = bad
        self.face1 = face1
        self.contador = 5

        # pygame.init()
        # tamaño de la apntalla
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.blit(pygame.image.load(f"images/{fondo1}").convert(), [0, 0])

        # musica fondo
        pygame.mixer.init()
        # self.play_background_music()

        pygame.display.set_caption("SERPIENCOVID GAME")
        # self.surface.fill((n1, n2, n3))
        self.snake = Snake(self.surface, 2, fondo1, face1)
        self.snake.draw()
        self.object = Object(self.surface, imagen, imagen2, bad)
        self.object.draw()

    @staticmethod
    # colisiones
    def is_collision(x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    '''def play_background_music(self):
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play()'''

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def play(self):

        self.snake.walk()
        self.object.draw()
        self.display_score()
        pygame.display.flip()

        # snake collision wiht the object1
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.object.x, self.object.y):
            self.play_sound("sounds/ding")
            # print("Colission")
            self.snake.increase_length()
            self.object.moveObject1()

        # snake collision wiht the object2
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.object.x2, self.object.y2):
            self.play_sound("sounds/ding")
            # print("Colission")
            self.snake.increase_length()
            self.object.moveObject2()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.object.x3, self.object.y3):
            self.play_sound("sounds/crash")
            self.contador = self.contador - 1
            # print(self.contador)
            # self.snake.reduce_length()
            self.object.moveObject3()

        # snake colLiding with itself
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("sounds/crash")
                raise Exception("Collision occured")

        '''if self.snake.length == 20:
            self.surface.fill((68,67,69))
            font = pygame.font.SysFont('arial', 30)
            line = font.render("¡¡You pass the level!!", True, (255, 255, 255))
            self.surface.blit(line, (200, 300))
            line3 = font.render("Press ESC, and choose the next level", True, (255, 255, 255))
            self.surface.blit(line3, (200, 350))
            pygame.display.flip()'''

    def show_game_over(self):
        # fondo de pantalla para cuando gameover
        self.surface.fill((68, 67, 69))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        # reset de los objects y de la sepriente para que empiece de 0
        self.snake = Snake(self.surface, 2, self.fondo1, self.face1)
        self.object = Object(self.surface, self.imagen, self.imagen2, self.bad)

    def display_score(self):
        # puntos por partida, insertar bbdd
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length - 2}", True, (255, 255, 255))
        self.surface.blit(score, (850, 10))
        # heart = pygame.image.load("heart30.jpeg").convert()
        # self.surface.blit(heart, [200, 10])
        lives = font.render(f"Lives: {self.contador}", True, (255, 255, 255))
        self.surface.blit(lives, (50, 10))
        # if self.contador == 5:

        if self.contador == 0:
            raise Exception("Collision occured")

    def run(self, tiempo):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        '''pygame.mixer.music.unpause()'''
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(tiempo)
