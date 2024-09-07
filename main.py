import pygame

pygame.init()
screen = pygame.display.set_mode((1200,720))
clock = pygame.time.Clock()
running = True

while running:
    # Poll for events
    # pygame.QUIT event means the user clicked C to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen
    screen.fill("purple")

    # RENDER THE GAME

    # flip() the display to put stuff on the screen
    pygame.display.flip()

    clock.tick(60) # limit FPS to 60

pygame.quit()
