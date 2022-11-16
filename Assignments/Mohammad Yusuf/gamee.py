import pygame



WIN = pygame.display.set_mode((900, 500))

def draw_window():
    WIN.fill((255,255,255))
    pygame.display.update()

pygame.display.set_caption("PY Game")
def gamee():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

# if __name__ == "__gamee__":
gamee()
   