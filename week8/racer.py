import random, sys, pygame
pygame.init()
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
STEP = 5
ENEMY_STEP = 10
BLACK = (0, 0, 0)
SCORE  = 0
SURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Yera's racer game")
clock = pygame.time.Clock()
global NUM_OF_COINS
NUM_OF_COINS=0
score_font = pygame.font.SysFont("Verdana", 20) 
bg = pygame.image.load("week8/AnimatedStreet.png") 


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("week8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 

    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1 
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("week8/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('week8/goldcoin.png')
        self.image=pygame.transform.scale(self.image,(25,25))
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0)
    def update(self):
        self.rect.move_ip(0,5)
        if(self.rect.bottom>SCREEN_HEIGHT):
            self.top=0
            self.rect.center=(random.randint(30,350),0)
    def spawn(self):
        self.rect.center=(random.randint(30,350),0)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
P1 = Player()
E1 = Enemy()
C1=Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins=pygame.sprite.Group()
coins.add(C1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.update()
    C1.update()
    
    if pygame.sprite.spritecollideany(P1, coins):
       NUM_OF_COINS+=1
       C1.spawn()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()

    SURF.blit(bg, (0, 0))
    score_img = score_font.render('Number of passing cars: '+str(SCORE), True, BLACK)
    coin_score_img=score_font.render('Number of collected coins: '+str(NUM_OF_COINS), True, BLACK)
    SURF.blit(score_img, (10, 10))
    SURF.blit(coin_score_img,(30,30)) 
    E1.draw(SURF)
    P1.draw(SURF)
    C1.draw(SURF)
    pygame.display.update()
    clock.tick(FPS)