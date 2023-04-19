import pygame
from random import randint
pygame.init()

W = 800
H = 600
FPS = 60
TILE = 32

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0,0,255)
wheat=(245,222,179)

red = (200, 0, 0)
light_red = (255, 0, 0)

yellow = (200, 200, 0)
light_yellow = (255, 255, 0)

green = (34, 177, 76)
light_green = (0, 255, 0)

window = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

fontUI = pygame.font.Font(None, 30)

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("Yu Mincho Demibold", 85)
vsmallfont = pygame.font.SysFont("Yu Mincho Demibold", 25)

imgBrick = pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/block_brick.png')
imgBackground = pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/grass_template2.jpg')
imgBackground = pygame.transform.scale(imgBackground, (W, H))
imgTanks = [
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/tank1.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/tank2.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/tank3.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/tank4.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/tank5.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/tank6.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/tank7.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/tank8.png'),
    ]
imgBangs = [
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/bang1.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/bang2.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/bang3.png'),
    ]
imgBonuses = [
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/bonus_star.png'),
    pygame.image.load('C:/Users/erasyl/Desktop/pp2/git/hackathon/images/bonus_tank.png'),
    ]

DIRECTS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

MOVE_SPEED =    [1, 2, 2, 1, 2, 3, 3, 2]
BULLET_SPEED =  [4, 5, 6, 5, 5, 5, 6, 7]
BULLET_DAMAGE = [1, 1, 2, 3, 2, 2, 3, 4]
SHOT_DELAY =    [60, 50, 30, 40, 30, 25, 25, 30]

class UI(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        i = 0
        for obj in objects:
            if obj.type == 'tank':
                pygame.draw.rect(window, obj.color, (5 + i * 70, 5, 22, 22))

                text = fontUI.render(str(obj.rank), 1, 'black')
                rect = text.get_rect(center = (5 + i * 70 + 11, 5 + 11))
                window.blit(text, rect)

                text = fontUI.render(str(obj.hp), 1, obj.color)
                rect = text.get_rect(center = (5 + i * 70 + 32, 5 + 11))
                window.blit(text, rect)
                i += 1
                

class Tank1(pygame.sprite.Sprite):
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.hp = 5
        self.shotTimer = 0

        self.moveSpeed = 2
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

        self.rank = 0
        self.image = pygame.transform.rotate(imgTanks[self.rank], -self.direct * 90)
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self):
        self.image = pygame.transform.rotate(imgTanks[self.rank], -self.direct * 90)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center = self.rect.center)

        self.moveSpeed = MOVE_SPEED[self.rank]
        self.shotDelay = SHOT_DELAY[self.rank]
        self.bulletSpeed = BULLET_SPEED[self.rank]
        self.bulletDamage = BULLET_DAMAGE[self.rank]
        
        oldX, oldY = self.rect.topleft
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):
        window.blit(self.image, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp == 0:
            objects.remove(self)
            print(self.color, 'dead')
            p1_win()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > W or self.py < 0 or self.py > H:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type != 'bang' and obj.type != 'bonus':
                    if obj.rect.collidepoint(self.px, self.py):
                        obj.damage(self.damage)
                        bullets.remove(self)
                        Bang(self.px, self.py)
                        break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)

class Tank2(pygame.sprite.Sprite):
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.hp = 5
        self.shotTimer = 0

        self.moveSpeed = 2
        self.shotDelay = 60
        self.bulletSpeed = 5
        self.bulletDamage = 1

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

        self.rank = 0
        self.image = pygame.transform.rotate(imgTanks[self.rank], -self.direct * 90)
        self.rect = self.image.get_rect(center = self.rect.center)

    def update(self):
        self.image = pygame.transform.rotate(imgTanks[self.rank], -self.direct * 90)
        self.image = pygame.transform.scale(self.image, (self.image.get_width() - 5, self.image.get_height() - 5))
        self.rect = self.image.get_rect(center = self.rect.center)

        self.moveSpeed = MOVE_SPEED[self.rank]
        self.shotDelay = SHOT_DELAY[self.rank]
        self.bulletSpeed = BULLET_SPEED[self.rank]
        self.bulletDamage = BULLET_DAMAGE[self.rank]
        
        oldX, oldY = self.rect.topleft
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
            self.direct = 3
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
            self.direct = 1
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
            self.direct = 0
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed
            self.direct = 2

        for obj in objects:
            if obj != self and obj.type == 'block' and self.rect.colliderect(obj.rect):
                self.rect.topleft = oldX, oldY

        if keys[self.keySHOT] and self.shotTimer == 0:
            dx = DIRECTS[self.direct][0] * self.bulletSpeed
            dy = DIRECTS[self.direct][1] * self.bulletSpeed
            Bullet(self, self.rect.centerx, self.rect.centery, dx, dy, self.bulletDamage)
            self.shotTimer = self.shotDelay

        if self.shotTimer > 0: self.shotTimer -= 1

    def draw(self):
        window.blit(self.image, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp == 0:
            objects.remove(self)
            print(self.color, 'dead')
            p2_win()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, parent, px, py, dx, dy, damage):
        bullets.append(self)
        self.parent = parent
        self.px, self.py = px, py
        self.dx, self.dy = dx, dy
        self.damage = damage

    def update(self):
        self.px += self.dx
        self.py += self.dy

        if self.px < 0 or self.px > W or self.py < 0 or self.py > H:
            bullets.remove(self)
        else:
            for obj in objects:
                if obj != self.parent and obj.type != 'bang' and obj.type != 'bonus':
                    if obj.rect.collidepoint(self.px, self.py):
                        obj.damage(self.damage)
                        bullets.remove(self)
                        Bang(self.px, self.py)
                        break

    def draw(self):
        pygame.draw.circle(window, 'yellow', (self.px, self.py), 2)


class Bang(pygame.sprite.Sprite):
    def __init__(self, px, py):
        objects.append(self)
        self.type = 'bang'

        self.px, self.py = px, py
        self.frame = 0

    def update(self):
        self.frame += 0.2
        if self.frame >= 3: objects.remove(self)

    def draw(self):
        image = imgBangs[int(self.frame)]
        rect = image.get_rect(center = (self.px, self.py))
        window.blit(image, rect)
    
class Block(pygame.sprite.Sprite):
    def __init__(self, px, py, size):
        objects.append(self)
        self.type = 'block'

        self.rect = pygame.Rect(px, py, size, size)
        self.hp = 1

    def update(self):
        pass

    def draw(self):
        window.blit(imgBrick, self.rect)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0: objects.remove(self)

class Bonus(pygame.sprite.Sprite):
    def __init__(self, px, py, bonusNum):
        objects.append(self)
        self.type = 'bonus'

        self.image = imgBonuses[bonusNum]
        self.rect = self.image.get_rect(center = (px, py))

        self.timer = 600
        self.bonusNum = bonusNum

    def update(self):
        if self.timer > 0: self.timer -= 1
        else: objects.remove(self)

        for obj in objects:
            if obj.type == 'tank' and self.rect.colliderect(obj.rect):
                if self.bonusNum == 0:
                    if obj.rank < len(imgTanks) - 1:
                        obj.rank += 1
                        objects.remove(self)
                        break
                elif self.bonusNum == 1:
                    obj.hp += 1
                    objects.remove(self)
                    break

    def draw(self):
        if self.timer % 30 < 15:
            window.blit(self.image, self.rect)

bullets = []
objects = []
P1 = Tank1('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))
P2 = Tank2('red', 650, 275, 0, (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_KP_ENTER))
ui = UI()
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                elif event.key == pygame.K_q:

                    pygame.quit()
                    quit()

        window.fill(black)
        message_to_screen("Welcome to Tanks!", white, -100, size="large")
        message_to_screen("The objective is to shoot and destroy", wheat, 15)
        message_to_screen("the enemy tank before they destroy you.", wheat, 60)
        message_to_screen("The more enemies you destroy, the harder they get.", wheat, 110)
        message_to_screen("Created by :- Team 15", wheat, 280)
        # message_to_screen("Press C to play, P to pause or Q to quit",black,180)


        button("Play", 150, 500, 100, 50, wheat, light_green, action="play",size="vsmall")
        
        button("Quit", 550, 500, 100, 50, wheat, light_red, action="quit",size="vsmall")

        pygame.display.update()

        clock.tick(15)
def button(text, x, y, width, height, inactive_color, active_color, action=None,size=" "):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(window, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()


            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

    else:
        pygame.draw.rect(window, inactive_color, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)

def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    if size == "vsmall":
        textSurface = vsmallfont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(W / 2), int(H / 2) + y_displace)
    window.blit(textSurf, textRect)

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="vsmall"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    window.blit(textSurf, textRect)

def pause():
    paused = True
    message_to_screen("Paused", white, -100, size="large")
    message_to_screen("Press C to continue playing or Q to quit", wheat, 25)
    pygame.display.update()
    while paused:
        #gameDisplay.fill(black)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)

for _ in range(50):
    while True:
        x = randint(0, W // TILE - 1) * TILE
        y = randint(1, H // TILE - 1) * TILE
        rect = pygame.Rect(x, y, TILE, TILE)
        fined = False
        for obj in objects:
            if rect.colliderect(obj.rect): fined = True

        if not fined: break

    Block(x, y, TILE)
def p1_win():
    win = True

    while win:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill(black)
        message_to_screen("P1 WIN!", white, -100, size="large")
        message_to_screen("Congratulations!", wheat, -30)

        #button("play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        button("quit", 350, 500, 100, 50, wheat, light_yellow, action="quit")
        #button("quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)
def p2_win():
    win = True

    while win:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill(black)
        message_to_screen("P2 WIN!", white, -100, size="large")
        message_to_screen("Congratulations!", wheat, -30)

        #button("play Again", 150, 500, 150, 50, wheat, light_green, action="play")
        button("quit", 350, 500, 100, 50, wheat, light_yellow, action="quit")
        #button("quit", 550, 500, 100, 50, wheat, light_red, action="quit")

        pygame.display.update()

        clock.tick(15)


def gameLoop():
    bonusTimer = 180
    global play
    play = True
    while play:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()
    

        global keys
        keys = pygame.key.get_pressed()


        if bonusTimer > 0:bonusTimer -= 1
        else:
            Bonus(randint(50, W - 50), randint(50, H - 50), randint(0, len(imgBonuses) - 1))
            bonusTimer = randint(120, 240)
    
        for bullet in bullets: 
            bullet.update()
        for obj in objects: 
            obj.update()
        ui.update()

        window.fill('black')
        for bullet in bullets: 
            bullet.draw()
        for obj in objects: 
            obj.draw()
        ui.draw()
    
        pygame.display.update()
        clock.tick(FPS)
        if P1.hp <= 0:
            p1_win()
        if P2.hp <= 0:
            p2_win()
    pygame.quit()
    quit()
game_intro()
gameLoop() 

