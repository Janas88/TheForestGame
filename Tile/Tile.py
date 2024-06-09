import pygame
import Level
import pygame.image
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, level, surface='Grass'):
        super().__init__()

        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft=(pos[1] * TILESIZE, pos[0] * TILESIZE))

        self.level = level
        self.pos = pos
        self.surface = surface
        self.contents = []


        if self.surface == "grass":
            self.image = pygame.image.load('Grass.png')
        elif self.surface == "dirt":
            self.image = pygame.image.load('Dirt.png')
    def add_thing(self, thing):
        thing.current_tile = self
        self.contents.append(thing)

    def remove_thing(self, thing):
        self.contents.remove(thing)

    def get_adjacent_tile(self, direction):
        row, col = self.pos
        if direction == 'up':
            row -= 1
        elif direction == 'down':
            row += 1
        elif direction == 'left':
            col -= 1
        elif direction == 'right':
            col += 1
        else:
            raise ValueError(f"Invalid direction: {direction}")

        return self.level.get_tile_at_position((row, col))

    def get_contents(self):
        return self.contents
    def has_player(self):
        for thing in self.contents:
            if thing.name == 'Player':
                return True
