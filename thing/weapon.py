import Thingmod

class Weapon(Thing):
    def __init__(self, name, size, weight, maxcapacity, place, acooldown, strength, mod):
        super().__init__(name, size, weight, maxcapacity, place)

        self.acooldown = acooldown
        self.dmg = strength
        self.mod = mod


    #graphics
    self.image = pygame.Surface((40,40))