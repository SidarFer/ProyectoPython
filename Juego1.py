
from tkinter import messagebox
import sys
import pygame
pygame.mixer.init()


pygame.init()

ventana = pygame.display.set_mode((640, 480))
font = pygame.font.Font(None, 36) # Fuente por defecto y tamaño
icono = pygame.image.load("bandera.png")
pygame.display.set_icon(icono)
pygame.display.set_caption("Juego de Bola Saltante")
campana = pygame.mixer.Sound('campana.mp3')
perder = pygame.mixer.Sound("perder.mp3")

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [4, 4]
ballrect.move_ip(0, 0)
# Crea el objeto bate, y obtengo su rectángulo
bate = pygame.image.load("guion.png")
baterect = bate.get_rect()
# Pongo el bate en la parte inferior de la pantalla
baterect.move_ip(200, 300)

#Comenzar el juego
contador = 0
perdedor = 10
jugando = True
while jugando:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3, 0)
    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3, 0)

    # Compruebo si hay colisión
    if baterect.colliderect(ballrect) and ballrect.colliderect(baterect):
        speed[1] = -speed[1]
        #Acá es la colisión
        campana.play()
        contador = contador + 1
        pygame.display.set_caption("Juego de Bola Saltante" + " :" + str(contador))
        if contador == 10:
            #Usted ha ganado
            messagebox.showinfo("Usted es un GANADOR !!!!!")
            sys.exit()

    #La Pelota no tocó el bate o pasó de su posición inferior
    if not ballrect.colliderect(baterect) and ballrect.top > baterect.bottom:
        print("❌ La pelota pasó el bate")
        #Usted ha Perdido
        perder.play()
        messagebox.showinfo(f"Usted ha Perdido !!!!!")
        sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        #Si la bola pegó en los bordes izquierdo o derecho de la ventana
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        #Si la bola pegó en los bordes superior o inferior de la ventana
        speed[1] = -speed[1]

    ventana.fill((0, 200, 200))
    ventana.blit(ball, ballrect)

    # Dibujo el bate
    ventana.blit(bate, baterect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

      
pygame.quit()

