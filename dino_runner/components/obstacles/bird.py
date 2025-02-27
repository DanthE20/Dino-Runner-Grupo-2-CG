from random import randint
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self, image):
        self.bird = BIRD[0]
        super().__init__(BIRD[0])
        self.rect.y = randint(200,300)
        self.step = 0

        
    def draw(self, screen):
        if self.step >= 9:
            self.step = 0
        screen.blit(BIRD[self.step // 5], self.rect)
        self.step += 1