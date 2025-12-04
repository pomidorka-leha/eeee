import pygame

class Game:
    screen = None
    aliens = []
    rockets = []
    lost = False
    
#Title#
    pygame.display.set_caption('Space Invaders')
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        done = False
        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        rocket = None
        while not done:
            if len(self.aliens) == 0:
                self.displayText("VICTORY")
    #Buttons and Hero vel#
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
                pygame.quit()
        if pressed[pygame.K_LEFT]:
            hero.x -= 2 if hero.x > 20 else 0
        elif pressed[pygame.K_RIGHT]:
            hero.x += 2 if hero.x < width - 20 else 0
    #SPACEBAR and rocket#
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                self.rockets.append(Rocket(self, hero.x, hero.y))
    #Visual Stuff (FPS, BG)
        pygame.display.flip()
        self.clock.tick(120)
        self.screen.fill((0, 0, 0))
    #DRAW Def and collision#
        for alien in self.aliens:
            alien.draw()
        alien.checkCollision(self)
        if (alien.y > height):
            self.lost = True
            self.displayText("YOU DIED")
        for rocket in self.rockets:
            rocket.draw()
        if not self.lost: hero.draw()
    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Monaco', 100)
        textsurface = font.render(text, False, (0, 128, 0))
        self.screen.blit(textsurface, (110, 160))
#ALIEN Proportions#
class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 35
    def draw(ALIEN):
        pygame.draw.rect(ALIEN.game.screen, (81, 43, 88),
        pygame.Rect(ALIEN.x, ALIEN.y, ALIEN.size, ALIEN.size))
        ALIEN.y += 0.15
    def checkCollision(ROCKET, game):
        for rocket in game.rockets:
            if (rocket.x < ROCKET.x + ROCKET.size and
            rocket.x > ROCKET.x - ROCKET.size and
            rocket.y < ROCKET.y + ROCKET.size and
            rocket.y > ROCKET.y - ROCKET.size):
                game.rockets.remove(rocket)
            game.aliens.remove(ROCKET)
#HERO#
class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
    def draw(self):
        pygame.draw.rect(self.game.screen,
        (180, 210, 255),
        pygame.Rect(self.x, self.y, 20, 15))

class Generator:
    def __init__(self, game):
        margin = 30
        width = 50
        for x in range(margin, game.width - margin, width):
            for y in range(margin, int(game.height / 2), width):
                game.aliens.append(Alien(game, x, y))
#WEAPON/ROCKET#
class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
    def draw(self):
        pygame.draw.rect(self.game.screen,
        (254, 52, 110),
        pygame.Rect(self.x, self.y, 5, 10))
        self.y -= 5
if __name__ == '__main__':
    game = Game(800, 600)