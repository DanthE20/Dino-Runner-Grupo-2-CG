import pygame
from random import randint
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS

class ObstacleManager:
    Y_SMALL_POS = 330
    Y_LARGE_POS = 305

    def __init__(self):
        self.obstacles = []

    def random_obstacles(self):
        generate_random_obstacle = randint(0, 2)
        if generate_random_obstacle == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS, self.Y_SMALL_POS))
        elif generate_random_obstacle == 1:
            self.obstacles.append(Cactus(LARGE_CACTUS, self.Y_LARGE_POS))
        else:
            self.obstacles.append(Bird(BIRD))

    def update(self, game):
        if len(self.obstacles) == 0:
            self.random_obstacles()

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)