from colors import Colors
import pygame
import random
import time
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect The apple")
clock = pygame.time.Clock()
score = 0

background = pygame.image.load(r"resources\images\background.png")
player = pygame.image.load(r"resources\images\player.png")
player = pygame.transform.scale(player, (150, 150))
apple = pygame.image.load(r"resources\images\apple.png")


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.vel = -5
        self.rect = player.get_rect()
        self.rect.x = x
        self.rect.y = y
character = Player(WIDTH / 2, HEIGHT / 2)

class Apple():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = apple.get_rect()
        self.rect.x = x
        self.rect.y = y

    def go_random(self):
        self.x = random.randint(0, WIDTH - self.rect.width)
        self.y = random.randint(0, HEIGHT - self.rect.height)
        time.sleep(0.1)
collecter = Apple(random.randint(32, WIDTH), random.randint(32, HEIGHT))

def render_game():
    global score

    character.x += character.change_x
    character.y += character.change_y
    character.rect.x = character.x
    character.rect.y = character.y
    collecter.rect.x = collecter.x
    collecter.rect.y = collecter.y

    screen.fill(Colors.GREEN.value)
    screen.blit(background, (0, 0))
    screen.blit(player, (character.x, character.y))
    screen.blit(apple, (collecter.x, collecter.y))
    clock.tick(FPS)
    Render_Text(r"resources\fonts\ComicNeue-Bold.ttf", str(round(clock.get_fps(), 2)), Colors.WHITE.value, (0, 0), screen)
    Render_Text(r"resources\fonts\ComicNeue-Bold.ttf", f"Score: {score}", Colors.WHITE.value, (WIDTH / 2, 0), screen)
    pygame.display.update()

def Render_Text(font, what, color, pos, window):
    font = pygame.font.Font(font, 20)
    text = font.render(what, 1, pygame.Color(color))
    window.blit(text, pos)
    

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.change_x = character.vel
            if event.key == pygame.K_RIGHT:
                character.change_x = abs(character.vel)
            if event.key == pygame.K_UP:
                character.change_y = character.vel
            if event.key == pygame.K_DOWN:
                character.change_y = abs(character.vel)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character.change_x = 0
            if event.key == pygame.K_RIGHT:
                character.change_x = 0
            if event.key == pygame.K_UP:
                character.change_y = 0
            if event.key == pygame.K_DOWN:
                character.change_y = 0


    if character.rect.colliderect(collecter.rect): 
        score += 1
        collecter.go_random()

    render_game()


pygame.quit()