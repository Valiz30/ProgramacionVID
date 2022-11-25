# Importar e inicializar Pygame.
from cmath import pi
import pygame
import tkinter as tk
import math
import random
from pygame.locals import *

class Bloque(pygame.sprite.Sprite):
    """
    Esta clase representa El objeto general de el juego.        
    Deriva de la clase "Sprite" en Pygame
    """
    def __init__(self, color, width, height, id):
        """ Constructor. Le pasa el color al bloque, 
        así como la posición de x,y """
        # Llama a la clase constructor padre (Sprite)
        super().__init__() 
  
        # Crea una imagen del bloque y lo rellena de color.
        # También podríamos usar una imagen guardada en disco.
        if(id == 0):
            self.image = pygame.Surface([width,height])
            self.image.fill(color)
            
        if(id == 1):
            self.image = pygame.Surface([96,96])
            self.image = pygame.image.load("pelota.png").convert()
            self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect() 
          
 
    def update(self, pos):
        """ Llamada para cada fotograma. """
 
        # Desplaza el bloque un píxel hacia abajo.
        self.rect.x == pos[0]
        self.rect.y == pos[1] 
pygame.init()
anchoPantalla = 800
altoPantalla = 600
tamPantalla = (anchoPantalla,altoPantalla)

# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode(tamPantalla)

# Poner el título de la ventana.
pygame.display.set_caption("Mi Juego")

# Crear la superficie del fondo o background.
imgBackground = pygame.Surface(screen.get_size())
imgBackground = imgBackground.convert()
fondo = (255, 221, 226)
imgBackground.fill(fondo)

# Inicializar las variables de control del game loop. 
clock = pygame.time.Clock() 
salir = False

bloque_lista = pygame.sprite.Group()
pelota = Bloque((0,0,0), 100, 100, 1)
pelota.rect.x = 350
pelota.rect.y = 250
bloque_lista.add(pelota)
barraIzquierda = Bloque((255, 131, random.randrange(131, 255, 3)), 10, 150, 0)
barraIzquierda.rect.x = 40
barraIzquierda.rect.y = 10
bloque_lista.add(barraIzquierda)
barraDerecha = Bloque((255, 131, random.randrange(131, 255, 3)), 10, 150, 0)
barraDerecha.rect.x = anchoPantalla - 50
barraDerecha.rect.y = 10
bloque_lista.add(barraDerecha)

sounds = []
sounds.append(pygame.mixer.Sound('song.mp3'))
sounds.append(pygame.mixer.Sound('song2.mp3'))
sounds[0].play()
direccionBarras = 0 #0 hacia abajo, 1 hacia arriba
direccionPelotaHorizontal = random.randrange(0, 2) #0 abajo, 1 arriba
direccionPelotaVertical = random.randrange(0, 2) #0 izquierda, 1 derecha
inicial = True
pixelesX = random.randrange(5, 11)
pixelesY = random.randrange(5, 11)

cont1 = 0
cont2 = 0 
while not salir:

    # Timer que controla el frame rate.
    clock.tick(30)

    # Procesar los eventos que llegan a la aplicación.
    for event in pygame.event.get():
        # Si se cierra la ventana se sale del programa.
        if event.type == pygame.QUIT:
            salir = True

        # Si se pulsa la tecla [Esc] se sale del programa.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                salir = True
# Actualizar la pantalla.
    recta1 = pygame.Rect(70, 10, 10, altoPantalla-20)
    recta2 = pygame.Rect(anchoPantalla - 80, 10, 10, altoPantalla-20)
    screen.blit(imgBackground, (0, 0))
    
    
    bloque_lista.draw(screen)
    pygame.draw.rect(screen, "#FF5C82", recta1)
    pygame.draw.rect(screen, "#FF5C82", recta2)
    #nueva posicion de las barras laterales
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if(barraIzquierda.rect.y <= 10):
            barraIzquierda.rect.y = barraIzquierda.rect.y + 10
        else:
            barraIzquierda.rect.y = barraIzquierda.rect.y - 10
    if keys[pygame.K_s]:
        if(barraIzquierda.rect.y >= altoPantalla - 160):
            barraIzquierda.rect.y = barraIzquierda.rect.y - 10
        else:
            barraIzquierda.rect.y = barraIzquierda.rect.y + 10
    if keys[pygame.K_UP]:
        if(barraDerecha.rect.y <= 10):
            barraDerecha.rect.y = barraDerecha.rect.y + 10
        else:
            barraDerecha.rect.y = barraDerecha.rect.y - 10
    if keys[pygame.K_DOWN]:
        if(barraDerecha.rect.y >= altoPantalla - 160):
            barraDerecha.rect.y = barraDerecha.rect.y - 10
        else:
            barraDerecha.rect.y = barraDerecha.rect.y + 10
    #si la pelota toca la barra izquierda
    impacto = pygame.sprite.collide_rect(pelota, barraIzquierda)
    if(impacto):
        direccionPelotaHorizontal = 1
    #si la pelota toca la barra derecha
    impacto = pygame.sprite.collide_rect(pelota, barraDerecha)
    if(impacto):
        direccionPelotaHorizontal = 0
    #Si la pelota toca el techo
    if(pelota.rect.y <= 0):
        direccionPelotaVertical = 0
    #Si la pelota toca el piso
    if(pelota.rect.y >= altoPantalla - 100):
        direccionPelotaVertical = 1  
    #Si la pelota pasa el limite de la barra izquierda
    distancia = pelota.rect.x - 10
    if(distancia <= 10):
        inicial = True
        cont2 = cont2 + 1
        sounds[1].play()
        print("Jugador 2:",cont2)
    #Si la pelota pasa el limite de la barra derecha
    distancia = (anchoPantalla - 30) - pelota.rect.x
    if(distancia <= 10):
        inicial = True
        cont1 = cont1 + 1
        sounds[1].play()
        print("Jugador 1:",cont1)
    #establece la nueva posicion de la pelota
    if inicial == True:
        pelota.rect.x = 350
        pelota.rect.y = 250
        direccionPelotaHorizontal = random.randrange(0, 2) #0 abajo, 1 arriba
        direccionPelotaVertical = random.randrange(0, 2) #0 izquierda, 1 derecha
        inicial = False
    else:
        if direccionPelotaHorizontal == 0:
            pelota.rect.x = pelota.rect.x - pixelesX
        if direccionPelotaHorizontal == 1:
            pelota.rect.x = pelota.rect.x + pixelesX
        if direccionPelotaVertical == 0:
            pelota.rect.y = pelota.rect.y + pixelesY
        if direccionPelotaVertical == 1:
            pelota.rect.y = pelota.rect.y - pixelesY
        pelota.update([pelota.rect.x,pelota.rect.y])
        
    
    
    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()
