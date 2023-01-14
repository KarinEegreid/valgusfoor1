# Karl Paju IS22 Ül1 Valgusfoori loomine
import pygame  # Pygame importimine

# Pygame käivitamine
pygame.init()
# Ekraani loomine
screen = pygame.display.set_mode([600, 600])  # Loob ekraani
# Ekraanile nime andmine
pygame.display.set_caption("Valgusfoor Karl Paju")  # paneb ekraanile nime

# Valgusfoori loomine
pygame.draw.rect(screen, [128, 128, 128], [100, 25, 100, 250], 3)  # loob ristküliku
pygame.draw.circle(screen, [0, 255, 0], [150, 230], 40, 0)  # loob punase ringi
pygame.draw.circle(screen, [255, 255, 0], [150, 150], 40, 0)  # loob kollase ringi
pygame.draw.circle(screen, [255, 0, 0], [150, 70], 40, 0)  # loob rohelise ringi

# Valgusfoori posti loomine ning postialuse
pygame.draw.line(screen, [128, 128, 128], [150, 500], [150, 270])  # posti loomine
pygame.draw.line(screen, [128, 128, 128], [100, 350], [150, 270])  # loob posti aluse vasakpoolse nurga
pygame.draw.line(screen, [128, 128, 128], [154, 275], [200, 350])  # loob posti aluse parempoolse nurga
pygame.draw.line(screen, [128, 128, 128], [200, 350], [100, 350])  # loob posti alusele aluse

# Eesti lipu loomine
pygame.draw.rect(screen, [0, 0, 102], [140, 300, 20, 30], 0)  # loob sinise ristküliku
pygame.draw.rect(screen, [255, 255, 255], [140, 320, 20, 10], 0)  # loob valge ristküliku
pygame.draw.rect(screen, [0, 0, 0], [140, 310, 20, 10], 0)  # loob musta rist küliku

pygame.display.flip()  # uuendab ekraani

# Loopi loomine
running = True  # running on tõene

while running:  # while käsu kasutamine ehk kui programm töötab

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # kui on False väärtus, siis sulgub programm
