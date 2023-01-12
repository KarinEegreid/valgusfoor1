#Karl Paju IS22 ÜL1 Valgusfoori loomine
import pygame
pygame.init()

screen=pygame.display.set_mode([300,300])
pygame.draw.rect(screen, [128,128,128], )





















running = True

# Loop
while running:

    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():

        # if event is of type quit then set
        # running bool to false
        if event.type == pygame.QUIT:
            running = False

