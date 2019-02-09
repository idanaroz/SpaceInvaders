import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

clock = pygame.time.Clock()
BULLET_SPEED = 10
invader_speed = 20
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)  # (RED, GREEN, BLUE)
BLACK = (0, 0, 0)
BULLET_RADIUS = 5
BULLET_SIZE = 10


clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("space invaders")


class Player(object):
    def __init__(self, size):
        self.size = size
        self.position = [int(WIDTH / 2), int(HEIGHT - 2 * size)]


player = Player(60)

invader_size = 40
invader_pos = [(440, 50), (400, 50), (420, 30)]


class Bullet(object):
    def __init__(self, size, player):
        self.pos = [int(player.position[0] + 30), int(player.position[1]) + 25]
        self.size = size

    def update_y_bullet_pos(self, player_pos):
        if self.pos[1] < 50:
            self.pos[1] = int(player_pos[1]) + 25

    def draw(self, color):
        pygame.draw.circle(SCREEN, color, (self.pos[0], self.pos[1]), BULLET_RADIUS, 0)


def iscollision(invader_pos, bullet_pos):
    if invader_pos[0] == bullet_pos[1]:  # need to get the y of invader position [0]
        return True
    return False


def update_y_bullet_pos(bullet_p, player_pos):
    if bullet_p[1] < 50:
        bullet_p[1] = int(player_pos[1]) + 25


game_over = False


def shoot_bullet(player):
    bullet = Bullet(BULLET_SIZE, player)
    while bullet.pos[1] > 50:
        # bullet is in the player position
        if bullet.pos[1] > int(player.position[1]):
            pygame.draw.circle(SCREEN, BLUE, (bullet.pos[0], bullet.pos[1]), BULLET_RADIUS, 0)
            bullet.pos[1] -= BULLET_SPEED

        if bullet.pos[1] < int(player.position[1]):
            pygame.draw.circle(SCREEN, RED, (bullet.pos[0], bullet.pos[1]), BULLET_RADIUS, 0)
            pygame.display.update()
            # time.sleep(100 / 1000) Todo: Remove this line
            pygame.time.delay(10)

            #  make the old one disappear
            pygame.draw.circle(SCREEN, BLACK, (bullet.pos[0], bullet.pos[1]), BULLET_RADIUS, 0)
            bullet.pos[1] -= BULLET_SPEED

            # format
            #     screen.fill(BLACK)


bullets = []


def redrawGameWindow():
    pygame.draw.rect(SCREEN, BLUE, (player.position[0], player.position[1], player.size, player.size),
                     0)  # [left, top, width, height]
    pygame.draw.polygon(SCREEN, GREEN, (invader_pos[0], invader_pos[1], invader_pos[2]), 0)
    # print(str(bullets))
    for bullet in bullets:
        bullet.draw(RED)
    pygame.display.update()

while not game_over:
    pygame.time.delay(10)

    for bullet in bullets:
        # bullet in the screen
        # print(str(bullet.pos))
        if bullet.pos[1] > 0 or bullet.pos[1] > HEIGHT:
            # draw black
            bullet.draw(BLACK)
            bullet.pos[1] -= BULLET_SPEED
        else:
            bullets.pop(bullets.index(bullet))


    for event in pygame.event.get():
        # #Escape
        # if event.type == pygame.QUIT:
        #     exit(0)

        # update bullet



        if event.type == pygame.KEYDOWN:  #CHeck it it is needed
            if event.key == pygame.K_ESCAPE:
                exit(0)

            x = player.position[0]
            y = player.position[1]

            if event.key == pygame.K_LEFT:  # Todo: idan - add boundries
                # delete old player position
                rect = (player.position[0], player.position[1], player.size, player.size)
                SCREEN.fill(BLACK, rect)

                x -= player.size

            if event.key == pygame.K_RIGHT:  # Todo: idan - add boundries

                # delete old player position
                rect = (player.position[0], player.position[1], player.size, player.size)
                SCREEN.fill(BLACK, rect)

                # update player pos
                x += player.size

            player.position = [x, y]

            #Shoot
            if event.key == pygame.K_SPACE:
                bullet = Bullet(BULLET_SIZE, player)
                bullets.append(bullet)

    redrawGameWindow()
