import pygame
import sys

# ---- Initialization ----
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Political Button Game")
clock = pygame.time.Clock()

# ---- Colors ----
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)      # Likud color
YELLOW = (255, 255, 50)    # Yesh Atid color

# ---- Function to draw a button ----
def draw_button(screen, color, rect, text):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.SysFont("Arial", 40, "bold")
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(rect[0]+rect[2]//2, rect[1]+rect[3]//2))
    screen.blit(text_surface, text_rect)

# ---- Buttons ----
buttons = [
    {"rect": pygame.Rect(100, 150, 180, 80), "color": BLUE, "text": "Likud", "message": "Bibi"},
    {"rect": pygame.Rect(320, 150, 180, 80), "color": YELLOW, "text": "Yesh Atid", "message": "Lapid"}
]

# ---- Game loop ----
running = True
while running:
    screen.fill(WHITE)
    
    # Draw buttons
    for btn in buttons:
        draw_button(screen, btn["color"], btn["rect"], btn["text"])
    
    pygame.display.flip()
    
    # ---- Event handling ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            mouse_pos = event.pos
            for btn in buttons:
                if btn["rect"].collidepoint(mouse_pos):
                    print(btn["message"])
    
    clock.tick(60)

pygame.quit()
sys.exit()