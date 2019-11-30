import pygame

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
running = True

x, y, r = -1, -1, 0
speed = 10
grow = False
timer = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            r = 0
            grow = True
    if grow:
        r += speed * timer.tick() / 1000
    screen.fill(pygame.Color('black'))
    pygame.draw.circle(screen, pygame.Color('red'), (x, y), int(r))
    pygame.display.flip()
