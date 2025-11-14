
import pygame

# Inicializar Pygame
pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 36) # Fuente por defecto y tamaño

# Definir las propiedades del botón
button_rect = pygame.Rect(100, 100, 150, 50) # (x, y, ancho, alto)
button_color = (0, 128, 255) # Azul
button_text = "Haz clic"
button_text_color = (255, 255, 255) # Blanco

# Crear el renderizado del texto una sola vez
button_text_surface = font.render(button_text, True, button_text_color)
button_text_rect = button_text_surface.get_rect(center=button_rect.center)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Comprobar si el clic está dentro del rectángulo del botón
            if button_rect.collidepoint(event.pos):
                print("Botón presionado") # Aquí iría la lógica que quieres ejecutar

    # Dibujar
    screen.fill((0, 0, 0)) # Fondo negro
    pygame.draw.rect(screen, button_color, button_rect) # Dibujar el botón
    screen.blit(button_text_surface, button_text_rect) # Dibujar el texto

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()