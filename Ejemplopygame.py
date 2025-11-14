
import pygame
pygame.init()

# --- Configuración básica ---
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejemplo de Botón en Pygame")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 120, 215)
AZUL_OSCURO = (0, 90, 160)
NEGRO = (0, 0, 0)

# Fuente
fuente = pygame.font.Font(None, 36)

# Crear rectángulo para el botón
boton = pygame.Rect(200, 150, 200, 60)

# --- Bucle principal ---
ejecutando = True
while ejecutando:
    pantalla.fill(BLANCO)
    
    # Obtener posición del mouse
    mouse = pygame.mouse.get_pos()
    
    # Cambiar color si el mouse está sobre el botón
    if boton.collidepoint(mouse):
        color_boton = AZUL_OSCURO
    else:
        color_boton = AZUL

    # Dibujar botón
    pygame.draw.rect(pantalla, color_boton, boton, border_radius=10)
    
    # Dibujar texto
    texto = fuente.render("JUGAR", True, BLANCO)
    pantalla.blit(texto, (boton.x + 60, boton.y + 15))
    
    # Revisar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton.collidepoint(evento.pos):
                print("¡Botón presionado! Aquí puedes cambiar de pantalla o iniciar el juego.")

    pygame.display.flip()

pygame.quit()