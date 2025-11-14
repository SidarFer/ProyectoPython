
import pygame
import subprocess

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de la Bolita y el Bate")


# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fuente para el texto
font = pygame.font.Font(None, 36)

# Posición y tamaño de la barra de menú
menu_bar_height = 30
menu_bar_rect = pygame.Rect(0, 0, screen_width, menu_bar_height)

# Opciones de menú
menu_options = ["Iniciar_Juego", "Salir"]
menu_items_pos = []

# Dibujar la barra de menú
pygame.draw.rect(screen, GRAY, menu_bar_rect)

# Dibujar las opciones del menú
x_offset = 10
for i, option in enumerate(menu_options):
    text_surf = font.render(option, True, BLACK)
    text_rect = text_surf.get_rect(topleft=(x_offset, 5)) # Ajuste para la altura del menú
    screen.blit(text_surf, text_rect)
    menu_items_pos.append((text_rect, option))
    x_offset += text_rect.width + 20 # Añadir espacio entre opciones

def reiniciar():
    subprocess.run(["python", "Juego1.py"])


# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for rect, option in menu_items_pos:
                if rect.collidepoint(event.pos):
                    #print(f"Se ha hecho clic en: {option}")
                    # Aquí se debe añadir la lógica de cada menú (por ejemplo, abrir un submenú)
                    if option == "Iniciar_Juego":
                        #print("Se Reinicia el Juego")
                        reiniciar()

                    elif option == "Salir":
                        exit()

    # Lógica de actualización de pantalla (borrar y redibujar para el juego principal)
    # screen.fill((0, 0, 0)) # Rellena el fondo del juego principal

    # Dibujar la barra de menú (siempre se dibujará encima)
    pygame.draw.rect(screen, GRAY, menu_bar_rect)
    for i, option in enumerate(menu_options):
        text_surf = font.render(option, True, BLACK)
        text_rect = text_surf.get_rect(topleft=(menu_items_pos[i][0].x, 5)) # Mantener la misma posición X
        screen.blit(text_surf, text_rect)

    pygame.display.flip()
    screen.fill((0, 200, 200))


pygame.quit()
