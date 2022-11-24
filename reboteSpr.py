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
    def __init__(self, color, width, height, centro, radio):
        """ Constructor. Le pasa el color al bloque, 
        así como la posición de x,y """
        # Llama a la clase constructor padre (Sprite)
        super().__init__() 
  
        # Crea una imagen del bloque y lo rellena de color.
        # También podríamos usar una imagen guardada en disco.
        self.image = pygame.Surface([width,height])
        #self.image.fill(color)
        pygame.draw.circle(self.image, color, centro, radio)
        self.image.set_colorkey((0,0,0))
        # Extraemos el objeto rectángulo que posee las dimensiones de la imagen.
        # Estableciendo los valores para rect.x and rect.y actualizamos la posición de este objeto.
        self.rect = self.image.get_rect(center = centro)    
 
    def update(self, pos):
        """ Llamada para cada fotograma. """
        self.rect.x = pos[0]
        self.rect.y = pos[1]
         
      

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
aux = pygame.sprite.Group()
#añade los bloques del mapa
anchoBloque = 30
pelota1 = Bloque((random.randrange(0, 255, 3), random.randrange(0, 255, 3), random.randrange(0, 255, 3)), anchoBloque, anchoBloque, (15,15), 15)
pelota1.rect.x = 10
pelota1.rect.y = 15
bloque_lista.add(pelota1)
pelota2 = Bloque((random.randrange(0, 255, 3), random.randrange(0, 255, 3), random.randrange(0, 255, 3)), anchoBloque, anchoBloque, (15,15), 15)
pelota2.rect.x = pelota1.rect.center[0] + 30
pelota2.rect.y = 15
bloque_lista.add(pelota2)
pelota3 = Bloque((random.randrange(0, 255, 3), random.randrange(0, 255, 3), random.randrange(0, 255, 3)), anchoBloque, anchoBloque, (15,15), 15)
pelota3.rect.x = pelota2.rect.center[0] + 54
pelota3.rect.y = 15
bloque_lista.add(pelota3)
pelota4 = Bloque((random.randrange(0, 255, 3), random.randrange(0, 255, 3), random.randrange(0, 255, 3)), anchoBloque, anchoBloque, (15,15), 15)
pelota4.rect.x = pelota3.rect.center[0] + 57
pelota4.rect.y = 15
bloque_lista.add(pelota4)
pelota5 = Bloque((random.randrange(0, 255, 3), random.randrange(0, 255, 3), random.randrange(0, 255, 3)), anchoBloque, anchoBloque, (15,15), 15)
pelota5.rect.x = pelota4.rect.center[0] + 93
pelota5.rect.y = 15
bloque_lista.add(pelota5)

#variables
velocidad1 = [5,5]
velocidad2 = [5,5]
velocidad3 = [5,5]
velocidad4 = [5,5]
velocidad5 = [5,5]
while not salir:

    # Timer que controla el frame rate.
    clock.tick(60)

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
    
    screen.blit(imgBackground, (0, 0))
    # Observamos si el bloque pelota ha colisionado con algo
    bloque_lista.remove(pelota1)
    listaImpacPelota = pygame.sprite.spritecollide(pelota1, bloque_lista, False)
    bloque_lista.add(pelota1)
    if(len(listaImpacPelota) >= 1):
        pelota1.update((random.randrange(15, anchoPantalla - 15, 3),15))
    bloque_lista.remove(pelota2)
    listaImpacPelota = pygame.sprite.spritecollide(pelota2, bloque_lista, False)
    bloque_lista.add(pelota2)
    if(len(listaImpacPelota) >= 1):
        pelota2.update((random.randrange(15, anchoPantalla - 15, 3),15))
    bloque_lista.remove(pelota3)
    listaImpacPelota = pygame.sprite.spritecollide(pelota3, bloque_lista, False)
    bloque_lista.add(pelota3)
    if(len(listaImpacPelota) >= 1):
        pelota3.update((random.randrange(15, anchoPantalla - 15, 3),15))
    bloque_lista.remove(pelota4)
    listaImpacPelota = pygame.sprite.spritecollide(pelota4, bloque_lista, False)
    bloque_lista.add(pelota4)
    if(len(listaImpacPelota) >= 1):
        pelota4.update((random.randrange(15, anchoPantalla - 15, 3),15))
    bloque_lista.remove(pelota5)
    listaImpacPelota = pygame.sprite.spritecollide(pelota5, bloque_lista, False)
    bloque_lista.add(pelota5)
    if(len(listaImpacPelota) >= 1):
        pelota5.update((random.randrange(15, anchoPantalla - 15, 3),15))

    bloque_lista.draw(screen)
    pelota1.update([pelota1.rect.x + velocidad1[0], pelota1.rect.y + velocidad1[1]])
    pelota2.update([pelota2.rect.x + velocidad2[0], pelota2.rect.y + velocidad2[1]])
    pelota3.update([pelota3.rect.x + velocidad3[0], pelota3.rect.y + velocidad3[1]])
    pelota4.update([pelota4.rect.x + velocidad4[0], pelota4.rect.y + velocidad4[1]])
    pelota5.update([pelota5.rect.x + velocidad5[0], pelota5.rect.y + velocidad5[1]])
    pelota = pelota1
    
    if(pelota.rect.x <= 0):
        if(velocidad1[0] < 0):
            velocidad1[0] = velocidad1[0] * -1
        else:
            velocidad1[0] = velocidad1[0]
    if(pelota.rect.x >= anchoPantalla - 30):
        if(velocidad1[0] > 0):
            velocidad1[0] = velocidad1[0] * -1
        else:
            velocidad1[0] = velocidad1[0]
    if(pelota.rect.y <= 0):
        if(velocidad1[1] < 0):
            velocidad1[1] = velocidad1[1] * -1
        else:
            velocidad1[1] = velocidad1[1]
    if(pelota.rect.y >= altoPantalla - 30):
        if(velocidad1[1] > 0):
            velocidad1[1] =  velocidad1[1] * -1
        else:
            velocidad1[1] = velocidad1[1]

    pelota = pelota2
    if(pelota.rect.x <= 0):
        if(velocidad2[0] < 0):
            velocidad2[0] = velocidad2[0] * -1
        else:
            velocidad2[0] = velocidad2[0]
    if(pelota.rect.x >= anchoPantalla - 30):
        if(velocidad2[0] > 0):
            velocidad2[0] = velocidad2[0] * -1
        else:
            velocidad2[0] = velocidad2[0]
    if(pelota.rect.y <= 0):
        if(velocidad2[1] < 0):
            velocidad2[1] = velocidad2[1] * -1
        else:
            velocidad2[1] = velocidad2[1]
    if(pelota.rect.y >= altoPantalla - 30):
        if(velocidad2[1] > 0):
            velocidad2[1] =  velocidad2[1] * -1
        else:
            velocidad2[1] = velocidad2[1]

    pelota = pelota3
    if(pelota.rect.x <= 0):
        if(velocidad3[0] < 0):
            velocidad3[0] = velocidad3[0] * -1
        else:
            velocidad3[0] = velocidad3[0]
    if(pelota.rect.x >= anchoPantalla - 30):
        if(velocidad3[0] > 0):
            velocidad3[0] = velocidad3[0] * -1
        else:
            velocidad3[0] = velocidad3[0]
    if(pelota.rect.y <= 0):
        if(velocidad3[1] < 0):
            velocidad3[1] = velocidad3[1] * -1
        else:
            velocidad3[1] = velocidad3[1]
    if(pelota.rect.y >= altoPantalla - 30):
        if(velocidad3[1] > 0):
            velocidad3[1] =  velocidad3[1] * -1
        else:
            velocidad3[1] = velocidad3[1]

    pelota = pelota4

    if(pelota.rect.x <= 0):
        if(velocidad4[0] < 0):
            velocidad4[0] = velocidad4[0] * -1
        else:
            velocidad4[0] = velocidad4[0]
    if(pelota.rect.x >= anchoPantalla - 30):
        if(velocidad4[0] > 0):
            velocidad4[0] = velocidad4[0] * -1
        else:
            velocidad4[0] = velocidad4[0]
    if(pelota.rect.y <= 0):
        if(velocidad4[1] < 0):
            velocidad4[1] = velocidad4[1] * -1
        else:
            velocidad4[1] = velocidad4[1]
    if(pelota.rect.y >= altoPantalla - 30):
        if(velocidad4[1] > 0):
            velocidad4[1] =  velocidad4[1] * -1
        else:
            velocidad4[1] = velocidad4[1]

    pelota = pelota5
    if(pelota.rect.x <= 0):
        if(velocidad5[0] < 0):
            velocidad5[0] = velocidad5[0] * -1
        else:
            velocidad5[0] = velocidad5[0]
    if(pelota.rect.x >= anchoPantalla - 30):
        if(velocidad5[0] > 0):
            velocidad5[0] = velocidad5[0] * -1
        else:
            velocidad5[0] = velocidad5[0]
    if(pelota.rect.y <= 0):
        if(velocidad5[1] < 0):
            velocidad5[1] = velocidad5[1] * -1
        else:
            velocidad5[1] = velocidad5[1]
    if(pelota.rect.y >= altoPantalla - 30):
        if(velocidad5[1] > 0):
            velocidad5[1] =  velocidad5[1] * -1
        else:
            velocidad5[1] = velocidad5[1]

    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()