import pygame

W, H = 10, 20
TILE = 20
GAME_RES = W * TILE, H * TILE

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
Clock = pygame.time.Clock()

while True:
    game_sc.fill(pygame.Color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    Clock.tick()
