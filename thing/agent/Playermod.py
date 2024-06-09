import pygame
from settings import *


class Player(Agent):
    def __init__(self, name, size, weight, maxcapacity, health, cooldownmod):
        super().__init__(name, size, weight, maxcapacity, health, cooldownmod)

    def input(self):
        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_s]:
            self.move('down', 10)
            print('up')
        elif keys[pygame.K_w]:
            self.move('up', 10)
        elif keys[pygame.K_d]:
            self.move('right', 10)
        elif keys[pygame.K_a]:
            self.move('left', 10)
        # attack input
        if keys[pygame.K_SPACE]:
            self.attack(20, 18)
        if keys[pygame.K_LCTRL]:
            print('magic')
