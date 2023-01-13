# Karl Paju IS22 Ül1 Valgusfoori loomine
import pygame

pygame.init()

screen = pygame.display.set_mode([300, 300])  # Loob ekraani
pygame.display.set_caption("Valgusfoor Karl Paju")  # paneb ekraanile nime
pygame.draw.rect(screen, [128, 128, 128], [100, 25, 100, 250], 3)  # loob ristküliku
pygame.draw.circle(screen, [0, 255, 0], [150, 230], 40, 0)  # loob punase ringi
pygame.draw.circle(screen, [255, 255, 0], [150, 150], 40, 0)  # loob kollase ringi
pygame.draw.circle(screen, [255, 0, 0], [150, 70], 40, 0)  # loob rohelise ringi

pygame.display.flip()  # uuendab ekraani

running = True  # running on tõene

# Loopi loomine
while running:  # while käsu kasutamine ehk kui programm töötab

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # kui on False väärtus, siis sulgub programm

