import pygame
from thing.Thingmod import Thing


class Agent(Thing):
    def __init__(self, name, size, weight, maxcapacity, health, cooldownmod=1):
        super().__init__(name, size, weight, maxcapacity)

        self.health = health
        self.cooldownmod = cooldownmod
        self.cooldown = 0

    def act(self, cooldown):
        self.cooldown += cooldown

    def move(self, direction, cooldown_value):
        adjacent_tile = self.current_tile.get_adjacent_tile(direction)
        if self.cooldown > 0:
            print(self.name + " cannot yet act!")
        elif adjacent_tile is not None:
            contents = adjacent_tile.get_contents()

            for thing in contents:
                if isinstance(thing, Agent) or thing.name == "Tree":
                    print("Collision! Cannot move to that tile.")
                    return
            self.move_self(adjacent_tile)
            self.cooldown += cooldown_value * self.cooldownmod
        else:
            print("Cannot move in that direction. Invalid tile.")

    def attack(self, cooldown_value, strength):
        if self.cooldown > 0:
            print(self.name + " cannot act yet!")
            return

        for direction in ("up", "down", "left", "right"):
            adjacent_tile = self.current_tile.get_adjacent_tile(direction)

            if adjacent_tile is not None:
                contents = adjacent_tile.get_contents()

                for thing in contents:
                    if isinstance(thing, Agent):
                        thing.receive_attack(strength)
                        print(f"{self.name} attacked {thing.name}!")
                        self.cooldown += cooldown_value * self.cooldownmod
                        break
            else:
                print("No agent to attack in that direction.")
        else:
            print("Cannot attack in that direction. Invalid tile.")

    def update_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def input(self):
        self.ai()

    def ai(self):
        pass
