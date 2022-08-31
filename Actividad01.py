# Importar e inicializar Pygame.
from cmath import pi
import pygame
import tkinter as tk
import math
#Creacion de la clase pelota
class Pelota:
    velocidad = 0
    posicion = [0,0]
    color = "nulo"
    pixelesRadio = 0
    def __init__(self, velocidad, posicion, color, pixelesRadio):
        self.velocidad = velocidad
        self.posicion = posicion
        self.color = color
        self.pixelesRadio = pixelesRadio
    def trazo(self, screen):
        pygame.draw.circle(screen, self.color, self.posicion, self.pixelesRadio)
        
pelotas = []
tamPantalla = (800,800)


def guardarDatos():
    totalPelotas = int(textoTotalP.get("1.0","end-1c"))
    colores = textoColor.get("1.0","end-1c").split(", ")
    velocidades = textoVelocidades.get("1.0","end-1c").split(", ")
    pixelesDesplazo = 800 / totalPelotas
    print(totalPelotas)
    print(colores)
    print(velocidades)
    for x in range(totalPelotas):
        posicionAux = [math.floor(pixelesDesplazo/2),math.floor((pixelesDesplazo*x)+math.floor(pixelesDesplazo/2))]
        pelotaAux = Pelota(int(velocidades[x]), posicionAux, colores[x], (math.floor(pixelesDesplazo/2)))
        pelotas.append(pelotaAux)
    
def mostrarAnimacion():
    #Iniciacilizacion de la ventana de pygame
    pygame.init()
    
    # Crear la ventana y poner el tamaño.
    screen = pygame.display.set_mode(tamPantalla)
    # Poner el título de la ventana.
    pygame.display.set_caption("Actividad 01")
    # Crear la superficie del fondo o background.
    imgBackground = pygame.Surface(screen.get_size())
    imgBackground = imgBackground.convert()
    imgBackground.fill((255, 221, 226))
    # Inicializar las variables de control del game loop. 


    clock = pygame.time.Clock() 
    salir = False
    # Loop principal (game loop) del juego.


    #pos =[ 50, 50]
    #velocidad=[5,0]
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
        for x in range(len(pelotas)):
            pelotas[x].trazo(screen)
            pelotas[x].posicion[0] = pelotas[x].posicion[0] + pelotas[x].velocidad
            #pos[0] = pos[0] + velocidad[0]
            #print(pos)
            '''Validar las posiciones o limites de la pantalla y el objeto
            Limite de los laterales
            '''
            #if(pelotas[x].posicion[0] < tamPantalla[0] - pelotas[x].pixelesRadio):
            #    pelotas[x].velocidad = 5
            if(pelotas[x].posicion[0] > tamPantalla[0] - pelotas[x].pixelesRadio):
                pelotas[x].velocidad = 0 
                #Limites Superior Inferior
            
            #if(pos[1] < 50):
            #    velocidad[1] = 0
            #if(pos[1] > tamPantalla[1] - 50):
            #    velocidad[1] = -0

    #pygame.draw.rect(screen, (255, 0, 0),[20|, 40], 0)
        pygame.display.flip()
    # Cerrar Pygame y liberar los recursos que pidió el programa. pygame.quit()
def accionBotonIngresar():
    guardarDatos()
    mostrarAnimacion()
    
#Creacion de la ventana que pide los datos
window = tk.Tk()
window.config(bg = "#FFDDE2")
window.geometry("500x500")
window.title("Datos")
window.resizable(width=False, height=False)
botonIngresar = tk.Button(window, text = "Ingresar Datos", bg = "#FF206E", fg= "white", border = 0, width = 25,  font=("Georgia", 18), command = accionBotonIngresar)
botonIngresar.place(x = 70, y = 430)
ingTotalP = tk.Label(window, text="Ingresa el total de pelotas", fg = "black", bg = "#FFDDE2",  font=("Georgia", 18))
ingTotalP.pack(pady=10)
textoTotalP = tk.Text(window, height = 1, width = 5, font=("Georgia", 16))
textoTotalP.pack(pady=10)
ingColor = tk.Label(window, text="Ingresa los colores, separados por (,).\nOrden: 1, 2, 3", fg = "black", bg = "#FFDDE2",  font=("Georgia", 18))
ingColor.pack(pady=10)
textoColor = tk.Text(window, height = 1, width = 20, font=("Georgia", 16))
textoColor.pack(pady=10)
ingVelocidades = tk.Label(window, text="Ingresa las velocidades, separados por (,).\nOrden: 1, 2, 3", fg = "black", bg = "#FFDDE2",  font=("Georgia", 18))
ingVelocidades.pack(pady=10)
textoVelocidades = tk.Text(window, height = 1, width = 20, font=("Georgia", 16))
textoVelocidades.pack(pady=10)
window = tk.mainloop()







