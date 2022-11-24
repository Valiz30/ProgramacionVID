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
            # Se agrega imagen
            self.image = pygame.Surface([32,32])
            self.image = pygame.image.load("santa.png").convert()
            self.image.set_colorkey((0,0,0))
        if(id == 2):
            # Se agrega imagen
            self.image = pygame.Surface([32,32])
            self.image = pygame.image.load("galleta.png").convert()
            self.image.set_colorkey((0,0,0))
        if(id == 3):
            # Se agrega imagen
            self.image = pygame.Surface([32,32])
            self.image = pygame.image.load("niño.png").convert()
            self.image.set_colorkey((0,0,0))
        # Extraemos el objeto rectángulo que posee las dimensiones de la imagen.
        # Estableciendo los valores para rect.x and rect.y actualizamos la posición de este objeto.
        self.rect = self.image.get_rect()
         
    def reset_pos(self):
        """ Restablecemos la posición en la parte alta de la pantalla, en una ubicación aleatoria x.
        Si hubiera una colisión, sería llamada por update() o por el bucle principal.
        """
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(700-20)        
 
    def update(self, pos):
        """ Llamada para cada fotograma. """
 
        # Desplaza el bloque un píxel hacia abajo.
        #self.rect.y += 1
         
        # Si el bloque estuviera muy abajo, lo restablecemos a la parte superior de la pantalla.
        
 
class Protagonista(Bloque):
    """ La clase protagonista deriva de Bloque, pero sobrescribe su funcionalidad de 'update' 
    por una nueva función de desplazamiento que moverá el bloque con el ratón. """
    def update(self, pos):
          
        # Extraemos x e y de la lista, tal como si extrajéramos letras de una cadena de texto (string).
        # Coloca al objeto protagonista en la posición del ratón.
        self.rect.x = pos[0]
        self.rect.y = pos[1]   

pygame.init()
anchoPantalla = 800
altoPantalla = 600
tamPantalla = (800,600)

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

# Esta es una lista de 'sprites.' Cada bloque en el programa es 
# añadido a esta lista. La lista bes gestionada por la clase llamada  'Group.'
bloque_lista = pygame.sprite.Group()
vacio = pygame.sprite.Group()
bloque_lista_galletas = pygame.sprite.Group()
bloque_lista_galletasAux = pygame.sprite.Group()
bloque_lista_galletasAux2 = pygame.sprite.Group()
bloque_lista_niños = pygame.sprite.Group()
# Esta es una lista de cada sprite, así como de los bloques y del protagonista.rojo
listade_todoslos_sprites= pygame.sprite.Group()

posxIni = 0
posyIni = 0 

#añade los bloques del mapa
for i in range(62):
    anchoBloque = 50
    bloque = Bloque((219, 48, 105), anchoBloque, 50, 0)
    # Establece una ubicación 
    bloque.rect.x = posxIni 
    bloque.rect.y = posyIni
    posxIni = posxIni + anchoBloque + 40
    if(posxIni > anchoPantalla):
        posyIni = posyIni + 90
        posxIni = 0
    
    # Añade el bloque a la lista de objetos
    bloque_lista.add(bloque)
    listade_todoslos_sprites.add(bloque)
#añade las galletas del mapa
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 55
bloque.rect.y = 5
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 325
bloque.rect.y = 5
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 505
bloque.rect.y = 5
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 700
bloque.rect.y = 55
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 145
bloque.rect.y = 95
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 400
bloque.rect.y = 145
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 145
bloque.rect.y = 300
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 505
bloque.rect.y = 550
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 234
bloque.rect.y = 551
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 235
bloque.rect.y = 250
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 235
bloque.rect.y = 10
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 500
bloque.rect.y = 400
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
bloque = Bloque(fondo, 32, 32, 2)
bloque.rect.x = 600
bloque.rect.y = 260
bloque_lista_galletas.add(bloque)
bloque_lista_galletasAux.add(bloque)
niño1 = Protagonista(fondo, 32, 32, 3)
niño1.rect.x = 415
niño1.rect.y = 120
bloque_lista_niños.add(niño1)
niño2 = Protagonista(fondo, 32, 32, 3)
niño2.rect.x = 50
niño2.rect.y = 150
bloque_lista_niños.add(niño2)
niño3 = Protagonista(fondo, 32, 32, 3)
niño3.rect.x = 595
niño3.rect.y = 40
bloque_lista_niños.add(niño3)
# Crea un bloque protagonista de color rojo
posJugador = [720, 540]
aux = [0,0]
protagonista = Protagonista(fondo, 20, 15, 1)
listade_todoslos_sprites.add(protagonista)

#Variables
posniño1 = [415, 120]
posniño3 = [595, 40]
posniño2 = [50, 150]
colision = False
cont = 0
puntaje = 0
bandera = 0
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
    color = (255, 131, random.randrange(131, 255, 3))
# Actualizar la pantalla.
    screen.blit(imgBackground, (0, 0))

    # Llamamos al método update() para cada sprite en la lista
    aux = posJugador
    listade_todoslos_sprites.update(posJugador)

    # Observamos si el bloque protagonista ha colisionado con algo
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, False)
    for bloque in lista_impactos_bloques:
        if keys[pygame.K_w]:
            posJugador[1] = posJugador[1] + 2
        if keys[pygame.K_s]:
            posJugador[1] = posJugador[1] - 2
        if keys[pygame.K_a]:
            posJugador[0] = posJugador[0] + 2
        if keys[pygame.K_d]:
            posJugador[0] = posJugador[0] - 2
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista_galletas, False)
    for bloque in lista_impactos_bloques:
        bloque_lista_galletas.remove(bloque)
        bloque_lista_galletasAux2.add(bloque)
        puntaje = puntaje + 5
        print("Tu puntaje es:" + str(puntaje))
    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista_niños, False)
    for bloque in lista_impactos_bloques:
        puntaje = puntaje - 5
        print("Tu puntaje es:" + str(puntaje))
        posJugador = [720, 540]
        listade_todoslos_sprites.update([720, 540])
        
    # Dibujamos todos los sprites
    listade_todoslos_sprites.draw(screen)
    bloque_lista_galletas.draw(screen)
    niño1.update(posniño1)
    niño2.update(posniño2)
    niño3.update(posniño3)
    bloque_lista_niños.draw(screen)
    
    # Nueva posicion de santa
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if(posJugador[1] <= 0):
            posJugador[1] = posJugador[1] + 1
        else:
            posJugador[1] = posJugador[1] - 2

    if keys[pygame.K_s]:
        if(posJugador[1] >= altoPantalla - 32):
            posJugador[1] = posJugador[1] - 1
        else:
            posJugador[1] = posJugador[1] + 2
    if keys[pygame.K_a]:
        if(posJugador[0] <= 0):
            posJugador[0] = posJugador[0] + 1
        else:
            posJugador[0] = posJugador[0] - 2
    if keys[pygame.K_d]:
        if(posJugador[0] >= anchoPantalla - 32):
            posJugador[0] = posJugador[0] - 1
        else:
            posJugador[0] = posJugador[0] + 2
    
    # Nueva posicion de niños horizontal
    if(cont < 60 and bandera == 0):
        posniño1[1] = posniño1[1] + 7
        posniño2[0] = posniño2[0] + 7
        posniño3[1] = posniño3[1] + 7
        cont = cont + 1
    if(cont < 60 and bandera == 1):
        posniño1[1] = posniño1[1] - 7
        posniño2[0] = posniño2[0] - 7
        posniño3[1] = posniño3[1] - 7
        cont = cont + 1
    if(cont >= 60 and bandera == 0):
        cont = 0
        bandera = 1
    if(cont >= 60 and bandera == 1):
        cont = 0
        bandera = 0

    if(puntaje == -5):
        bloque_lista_galletas.add(bloque_lista_galletasAux2)
        puntaje = 0 
        print("Perdiste")
    
    if(len(bloque_lista_galletas) == 0):
        print("Ganaste")
        bloque_lista_galletas.add(bloque_lista_galletasAux2)
        puntaje = 0 
        posJugador = [720, 540]
        listade_todoslos_sprites.update([720, 540])
    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()