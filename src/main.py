import pygame
import sys
import os  # Para construir rutas relativas

# Ruta base de los recursos
BASE_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(BASE_DIR, "../assets/images")
SOUNDS_DIR = os.path.join(BASE_DIR, "../assets/sounds")

# Inicialización
pygame.init()

ANCHO, ALTO = 800, 600
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Boliranota - TEst")
fuente = pygame.font.SysFont("Arial", 20)

# Cargar fondo e imagen con rutas actualizadas
fondo_path = os.path.join(IMAGES_DIR, "img.jpeg")
fondo = pygame.image.load(fondo_path)
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Cargar sonido con ruta actualizada
sonido_path = os.path.join(SOUNDS_DIR, "frog.mp3")
sonido_punto = pygame.mixer.Sound(sonido_path)

jugadores = {
    "JUGADOR 1": 0,
    "JUGADOR 2": 0,
    "JUGADOR 3": 0,
    "JUGADOR 4": 0,
}
jugador_nombres = list(jugadores.keys())
jugador_actual_idx = 0
jugador_actual = jugador_nombres[jugador_actual_idx]

estrellas = [
    {"pos": (400, 200), "valor": 20, "r": 30},
    {"pos": (350, 270), "valor": 40, "r": 30},
    {"pos": (450, 270), "valor": 60, "r": 30},
    {"pos": (400, 340), "valor": 80, "r": 30},
    {"pos": (300, 200), "valor": 100, "r": 30},
    {"pos": (500, 200), "valor": 120, "r": 30},
]

boton_rect = pygame.Rect(600, 50, 150, 40)

def dibujar_estrellas():
    for estrella in estrellas:
        x, y = estrella["pos"]
        r = estrella["r"]
        pygame.draw.circle(pantalla, BLANCO, (x, y), r)
        pygame.draw.circle(pantalla, NEGRO, (x, y), r, 2)
        texto_valor = fuente.render(str(estrella["valor"]), True, NEGRO)
        pantalla.blit(texto_valor, (x - 10, y - 10))

def mostrar_puntajes():
    y = 50
    for nombre, puntos in jugadores.items():
        texto = fuente.render(f"{nombre}: {puntos} pts", True, NEGRO)
        pantalla.blit(texto, (50, y))
        y += 30

def mostrar_jugador_actual():
    texto = fuente.render(f"Turno: {jugador_actual}", True, NEGRO)
    pantalla.blit(texto, (600, 20))

def detectar_click(pos):
    global jugadores
    for estrella in estrellas:
        x, y = estrella["pos"]
        r = estrella["r"]
        dx = pos[0] - x
        dy = pos[1] - y
        if dx*dx + dy*dy <= r*r:
            jugadores[jugador_actual] += estrella["valor"]
            sonido_punto.play()
            break

def dibujar_boton():
    pygame.draw.rect(pantalla, (200, 200, 255), boton_rect)
    texto = fuente.render("Cambiar Jugador", True, NEGRO)
    pantalla.blit(texto, (boton_rect.x + 10, boton_rect.y + 10))

def cambiar_jugador():
    global jugador_actual_idx, jugador_actual
    jugador_actual_idx = (jugador_actual_idx + 1) % len(jugador_nombres)
    jugador_actual = jugador_nombres[jugador_actual_idx]

reloj = pygame.time.Clock()

while True:
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_rect.collidepoint(evento.pos):
                cambiar_jugador()
            else:
                detectar_click(evento.pos)

    mostrar_puntajes()
    dibujar_estrellas()
    mostrar_jugador_actual()
    dibujar_boton()

    pygame.display.flip()
    reloj.tick(60)
