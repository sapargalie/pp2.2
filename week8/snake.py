#collision check with the walls that appear on the 2nd level
#ordinary food
import pygame
import random
green=(0,100,0)
black=(0,0,0)
red=(255,0,0)
grey=(69,69,69)
yellow=(250,253,15)
pygame.init()
window_width,window_height=500,500
screen=pygame.display.set_mode((window_width,window_height))
class Snake:
    def __init__(self, x, y):
        self.size = 1
        self.elements = [[x, y]]  
        self.radius = 10
        self.dx = 5 
        self.dy = 0
        self.add_size = False
        self.speed = 25
        self.score=0
        self.level=1
        self.running=True
        self.font=pygame.font.SysFont("comicsansms", 20)
    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (black), element, self.radius)
    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.add_size = False
    def message1(self):
        text1 = self.font.render("Current level: "+str(self.level), True,black)
        return text1
    def message2(self):
        text2 = self.font.render("Current score: "+str(self.score), True,black)
        return text2
    def message3(self):
        text3 = self.font.render("Current speed: "+str(self.speed), True,black)
        return text3
    def move(self):
        if self.add_size:
            self.add_to_snake()
        #this for loop makes every part of the snake go after her head
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        #self.elements[0][0] it s the x position of the head
        #self.elements[0][1] it s the y
        #this two lines move the head
        self.elements[0][0] += self.dx
        self.elements[0][1]+= self.dy

        #so that the snake would return when leaving the playing area
        if self.elements[0][0] > window_width: 
            self.elements[0][0]=0 
        elif self.elements[0][0]<0: 
            self.elements[0][0]=window_width
        if self.elements[0][1] >window_height: 
            self.elements[0][1] =0
        elif self.elements[0][1]<0: 
            self.elements[0][1]=window_height
    #so that when the snake's head touches the walls it's game over
    def collision_check(self):
        if snake.level>=2:
            if self.elements[0][0]>=300 and self.elements[0][0]<=340 and self.elements[0][1]>=0 and self.elements[0][1]<=150:
                self.running=False
            elif self.elements[0][0]>=150 and self.elements[0][0]<=200 and self.elements[0][1]>=300 and self.elements[0][1]<=window_height:
                self.running=False
            return self.running
        else:
            return self.running
    #checking if the head touched the food,adding speed on new levels and adding scores
    #returns boolean value for generating new food possible
    def eat(self, foodx1, foody1):
        if foodx1 <= self.elements[0][0] <= foodx1 + 10 and foody1 <= self.elements[0][1] <= foody1 + 10:
            self.score+=1
            #every 3 points, the level increases, speed of the snake increases by 5 with every level
            if self.score % 3 == 0:
                self.speed += 5 #
                self.level+=1
            return True
        return False  
    #so that walls would only appear on the 2nd level and stay there
    def walls(self):
        if self.level>=2:
            return True
class Food:
    def __init__(self):
        self.x = random.randint(1, window_width)
        self.y = random.randint(1, window_height)

    def gen(self):
        self.x = random.randint(1, window_width)
        self.y = random.randint(1, window_height)
        #when it's 2nd level food shouldn't appear on the walls
        if snake.level>=2:
            if self.x>=300 and self.x<=340:
                self.y=random.randint(151,window_height)
            elif self.x>=150 and self.x<=200:
                self.y=random.randint(1,300)
    def draw(self):
        pygame.draw.rect(screen, red, (self.x, self.y, 10, 10))

snake = Snake(100, 100) #100,100 is the initial position of snake always
food1 = Food()
FPS = 30
d = 5
clock = pygame.time.Clock()
running=True
while snake.collision_check() and running:
    clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT and snake.dx != -d:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx != d:
                snake.dx = -d
                snake.dy = 0
            if event.key == pygame.K_UP and snake.dy != d:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN and snake.dy != -d:
                snake.dx = 0
                snake.dy = d
    if snake.eat(food1.x, food1.y):
        snake.add_size = True
        food1.gen()
    snake.move()
    screen.fill(green)
    screen.blit(snake.message1(),(10,10))
    screen.blit(snake.message2(),(10,30))
    screen.blit(snake.message3(),(10,50))
    if(snake.walls()):
        pygame.draw.rect(screen,grey, pygame.Rect(300,0,40,150))
#syntax pygame.draw.rect(surface, color, pygame.Rect(leftx,lefty,width,height))
        pygame.draw.rect(screen,grey,pygame.Rect(150,300,50,200))
    snake.draw()
    food1.draw()
    pygame.display.flip()
pygame.quit()