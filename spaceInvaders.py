import pygame
import time
from pygame.locals import *

pygame.init()

width = 800
height = 600

clock = pygame.time.Clock()
speed = 10
invader_speed = 20
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0) #(RED, GREEN, BLUE)
BLACK = (0,0,0)
player_size = 50
player_position = [int(width / 2), int(height - 2 * player_size)]
bullet_size = 10
bullet_pos = [int(player_position[0] + 30), int(player_position[1]) + 25]
BULLET_RADIUS = 5
invader_size = 40
invader_pos = [(440, 50), (400, 50), (420, 30)]


clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))


pygame.display.set_caption("SPACE INVADERS") #` Add title to the screen (put whatever you want guy)


def iscollision(invader_pos, bullet_pos):
    if invader_pos[0] == bullet_pos[1]:  # need to get the y of invader position [0]
        return True
    return False

def update_y_bullet_pos(bullet_p, player_pos):
    if bullet_p[1] < 50:
        bullet_p[1] = int(player_pos[1]) + 25

game_over = False
while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit(0)

            x = player_position[0]
            y = player_position[1]

            if event.key == pygame.K_LEFT:  # Todo: idan - add boundries
                # delete old player position
                rect = (player_position[0], player_position[1], player_size, player_size)
                screen.fill(BLACK, rect)
                if player_position[0] >= 1:
                    x -= player_size
                    bullet_pos[0] -= player_size
                update_y_bullet_pos(bullet_pos,player_position)
            if event.key == pygame.K_RIGHT:  # Todo: idan - add boundries

                # delete old player position
                rect = (player_position[0], player_position[1], player_size, player_size)
                screen.fill(BLACK, rect)

                # update player pos
                if player_position[0] <= width - player_size -1:
                    x += player_size
                    bullet_pos[0] += player_size
                update_y_bullet_pos(bullet_pos, player_position)

            player_position = [x, y]

            if event.key == pygame.K_SPACE:
                while bullet_pos[1] > 0:
                    # bullet is in the player position
                    if bullet_pos[1] > int(player_position[1]):
                        pygame.draw.circle(screen, BLUE, (bullet_pos[0], bullet_pos[1]), BULLET_RADIUS, 0)
                        bullet_pos[1] -= speed

                    if bullet_pos[1] < int(player_position[1]):
                        pygame.draw.circle(screen, RED, (bullet_pos[0], bullet_pos[1]), BULLET_RADIUS, 0)
                        pygame.display.update()
                        # time.sleep(100 / 1000) Todo: Remove this line
                        pygame.time.delay(10) #idan added this line  TODO: PLEASE delete this comment after you notice it

                        #  make the old one disappear
                        pygame.draw.circle(screen, BLACK, (bullet_pos[0], bullet_pos[1]), BULLET_RADIUS, 0)
                        bullet_pos[1] -= speed

# format
#     screen.fill(BLACK)
    player = pygame.draw.rect(screen, BLUE, (player_position[0], player_position[1], player_size, player_size), 0) #[left, top, width, height]
    invader = pygame.draw.polygon(screen, GREEN, (invader_pos[0], invader_pos[1], invader_pos[2]), 0)
    # bullet = pygame.draw.circle(screen, RED, (bullet_pos[0], bullet_pos[1]), BULLET_RADIUS, 0) #Todo: remove this line

    pygame.display.update()