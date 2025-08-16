import pygame
import random

pygame.init()
uzunluq, en = 1000, 500
screen = pygame.display.set_mode((uzunluq, en))
pygame.display.set_caption("The Mel1kovhs Team")

# İlan
ilanin_basi = [100, 50]
ilanin_beden_hissesidir = [[200, 100], [180, 100], [160, 100]]
ilanin_rengidir = (0, 0, 0)

# Meyvə
meyve_poz = [random.randrange(1, uzunluq // 10) * 10,
             random.randrange(1, en // 10) * 10]
meyve_rengi = (255, 0, 0)

# İstiqamət
istiqameti = "RIGHT"
istiqameti_deyis = istiqameti

clock = pygame.time.Clock()
isleme = True

while isleme:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isleme = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and istiqameti != "DOWN":
                istiqameti_deyis = "UP"
            elif event.key == pygame.K_DOWN and istiqameti != "UP":
                istiqameti_deyis = "DOWN"
            elif event.key == pygame.K_RIGHT and istiqameti != "LEFT":
                istiqameti_deyis = "RIGHT"
            elif event.key == pygame.K_LEFT and istiqameti != "RIGHT":
                istiqameti_deyis = "LEFT"

    istiqameti = istiqameti_deyis

    # İlanın hərəkəti
    if istiqameti == "UP":
        ilanin_basi[1] -= 10
    elif istiqameti == "DOWN":
        ilanin_basi[1] += 10
    elif istiqameti == "RIGHT":
        ilanin_basi[0] += 10
    elif istiqameti == "LEFT":
        ilanin_basi[0] -= 10

    ilanin_beden_hissesidir.insert(0, list(ilanin_basi))

    # Meyvə yeyiləndə böyüsün
    if ilanin_basi == meyve_poz:
        meyve_poz = [random.randrange(1, uzunluq // 10) * 10,
                     random.randrange(1, en // 10) * 10]
    else:
        ilanin_beden_hissesidir.pop()

    # Ekranı rənglə doldur
    screen.fill((137, 207, 240))

    # Meyvəni çək
    pygame.draw.rect(screen, meyve_rengi, pygame.Rect(meyve_poz[0], meyve_poz[1], 10, 10))

    # İlanı çək
    for hiss in ilanin_beden_hissesidir:
        pygame.draw.rect(screen, ilanin_rengidir, pygame.Rect(hiss[0], hiss[1], 10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()



