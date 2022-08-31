# Importar e inicializar Pygame.
from functools import total_ordering
import pygame
import tkinter as tk
import math
import random
#Creacion de la clase pelota    
class Pelota:
    id = 0
    velocidad = [0,0]
    posicion = [0,0]
    color = (0,0,0)
    pixelesRadio = 0
    banderas = []
    contChoque = 0
    def __init__(self, id, velocidad, posicion, pixelesRadio, banderas):
        self.velocidad = [velocidad,velocidad]
        self.posicion = posicion
        self.color = (random.randrange(0, 255, 3), random.randrange(0, 255, 3), random.randrange(0, 255, 3))
        self.pixelesRadio = pixelesRadio
        self.id = id
        self.banderas = banderas
    def trazo(self, screen):
        pygame.draw.circle(screen, self.color, self.posicion, self.pixelesRadio)
Pelotas = []
totalPelotas = random.randrange(2, 10, 2)



pygame.init()
tamPantalla = (800,600)
# Crear la ventana y poner el tamaño.
screen = pygame.display.set_mode(tamPantalla)
# Poner el título de la ventana.
pygame.display.set_caption("Mi Juego")

# Crear la superficie del fondo o background.
imgBackground = pygame.Surface(screen.get_size())
imgBackground = imgBackground.convert()
imgBackground.fill((255, 221, 226))
# Inicializar las variables de control del game loop. 
clock = pygame.time.Clock() 
salir = False
# Loop principal (game loop) del juego.
banderasAux = []

for y in range(totalPelotas):
    banderasAux.append(0)
for x in range(totalPelotas):
    PelotaAux = Pelota(x, random.randrange(3, 8, 1), [random.randrange(50, tamPantalla[0] - 50, 3),50], 50, banderasAux)
    Pelotas.append(PelotaAux)
    
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
    for x in range(totalPelotas):
        Pelotas[x].trazo(screen)
        #Comparacion de la posicion de las pelotas
        for y in range(totalPelotas):
            if(Pelotas[x].id != Pelotas[y].id):
                distancia = math.floor(math.sqrt(((Pelotas[x].posicion[1] - Pelotas[x].posicion[0])**2)+((Pelotas[y].posicion[1] - Pelotas[y].posicion[0])**2)))
                if(distancia < 100 and Pelotas[x].banderas[y] == 0):
                    Pelotas[x].banderas[y] = 1
                    Pelotas[y].banderas[x] = 1
                    Pelotas[x].contChoque += 1
                    Pelotas[y].contChoque += 1
                    print("La pelota "+ str(Pelotas[x].id)+" choco con la pelota "+ str(Pelotas[y].id))
                    print("Pelota " + str(x) + "- total choques : " + str(Pelotas[x].contChoque))
                    print("Pelota " + str(y) + "- total choques : " + str(Pelotas[y].contChoque))
                if(distancia > 100 and Pelotas[x].banderas[y] == 1):  
                    Pelotas[x].banderas[y] = 0
                    Pelotas[y].banderas[x] = 0
                
                    
        Pelotas[x].posicion[1] = Pelotas[x].posicion[1] + Pelotas[x].velocidad[1]
        Pelotas[x].posicion[0] = Pelotas[x].posicion[0] + Pelotas[x].velocidad[0]
        '''Validar las posiciones o limites de la pantalla y el objeto
        Limite de los laterales
        '''
        if(Pelotas[x].posicion[0] < 50):
            if(Pelotas[x].velocidad[0] < 0):
                Pelotas[x].velocidad[0] = Pelotas[x].velocidad[0] * -1
            else:
                Pelotas[x].velocidad[0] = Pelotas[x].velocidad[0]
        if(Pelotas[x].posicion[0] > tamPantalla[0] - 50):
            if(Pelotas[x].velocidad[0] > 0):
                Pelotas[x].velocidad[0] =  Pelotas[x].velocidad[0] * -1
            else:
                Pelotas[x].velocidad[0] = Pelotas[x].velocidad[0]
        #Limites Superior Inferior
        if(Pelotas[x].posicion[1] < 50):
            if(Pelotas[x].velocidad[1] < 0):
                Pelotas[x].velocidad[1] = Pelotas[x].velocidad[1] * -1
            else:
                Pelotas[x].velocidad[1] = Pelotas[x].velocidad[1]
        if(Pelotas[x].posicion[1] > tamPantalla[1] - 50):
            if(Pelotas[x].velocidad[1] > 0):
                Pelotas[x].velocidad[1] =  Pelotas[x].velocidad[1] * -1
            else:
                Pelotas[x].velocidad[1] = Pelotas[x].velocidad[1]

    #pygame.draw.rect(screen, (255, 0, 0),[20|, 40], 0)
    pygame.display.flip()
# Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()