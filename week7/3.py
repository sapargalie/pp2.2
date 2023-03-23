import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
running = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
clock = pygame.time.Clock()
FPS = 60
x=25
y=25
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP and y-50>=0:
               y-=20
            if event.key==pygame.K_DOWN and y+50<=500:
                y+=20
            if event.key==pygame.K_LEFT and x-50>=0:
                x-=20   
            if event.key==pygame.K_RIGHT and x+50<=500:
                x+=20
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)
    pygame.display.flip()
    clock.tick(FPS)