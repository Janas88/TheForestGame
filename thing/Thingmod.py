import Tile
import pygame

class Thing:
    def __init__(self, name, size, weight, maxcapacity=0):

        self.name = name
        self.size = size
        self.weight = weight
        self.maxcapacity = maxcapacity
        self.capacity = maxcapacity
        self.contents = []
        self.current_tile = None
        self.sprite = None
        self.health = 10000

    def add_thing_to_inventory(self, thing):
        if thing.size > self.capacity:
            print(thing.name + " is too large!")
        else:
            self.capacity = self.capacity - thing.size
        self.contents.append(thing)

    def remove_thing_from_inventory(self, thing):
        self.contents.remove(thing)

    def move_self(self, newtile):
        self.current_tile.remove_thing(self)
        newtile.add_thing(self)

    def assign_sprite(self, sprite_file):
        sprite_image = pygame.image.load(sprite_file)

        sprite_image = pygame.transform.scale(sprite_image, (64, 64))

        sprite = pygame.sprite.Sprite()
        sprite.image = sprite_image
        sprite.rect = sprite_image.get_rect()

        self.sprite = sprite

        return sprite

    def get_sprite(self):
        return self.sprite

    def receive_attack(self, strength):
        self.health -= strength
        print(f"{self.name} received an attack. Health: {self.health}")
        if self.health <= 0:
            self.current_tile.remove_thing(self)