from thing.Thingmod import Thing
from thing.agent.Agentmod import Agent
from thing.agent.Playermod import Player
from types import MethodType

WIDTH = 1280
HEIGHT = 720
FPS = 30
TILESIZE = 64
CONSOLE_WIDTH = WIDTH
CONSOLE_HEIGHT = 200
CONSOLE_FONT_SIZE = 16
CONSOLE_FONT_COLOR = (255, 255, 255)
CONSOLE_BG_COLOR = (0, 0, 0)
FONT_PATH = "Merchant Copy.ttf"
WORLD_MAP = [
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'd', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'd', 'd', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'd', 'd', 'd', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'd', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'd', 'd', 'd', 'd', 'd', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'd', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'd', 'd', 'g', 'g', 'g', 'd', 'd', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
    ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'd', 'd', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
]

POPULATE_MAP = [
    ['x', 'x', 'x', 't', 't', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 's', 'x', 't', 'x', 't', 'x', 't', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 't', 'x', 't', 'x', 'x', 'x'],
    ['x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x'],
    ['x', 't', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'w', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'w', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'w', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 't', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x'],
    ['x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 't', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 't', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 't', 't', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'h', 'x', 't', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 't', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'p', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
]

TILE_INTERPRETATION = {
    'g': 'grass',
    'd': 'dirt',
    'x': 'empty',
    'p': lambda level, row, col: GeneratePlayer(level, row, col, 'player.png'),
    't': lambda level, row, col: GenerateTree(level, row, col, 'tree.png'),
    'b': lambda level, row, col: GenerateBranch(level, row, col, 'branch.png'),
    'w': lambda level, row, col: GenerateWolf(level, row, col, 'wolf.png'),
    's': lambda level, row, col: GenerateSquirrel(level, row, col, 'squirrel.png'),
    'h': lambda level, row, col: GenerateHermit(level, row, col, 'hermit.png'),

}


def GeneratePlayer(level, row, col, sprite_file):
    player = Player(name='Player', size=1, weight=10, maxcapacity=400, health=100, cooldownmod=0.9)
    tile = level.tile_grid[row][col]
    tile.add_thing(player)
    player.assign_sprite(sprite_file)
    return player


def GenerateTree(level, row, col, sprite_file):
    tree = Thing(name='Tree', size=1000, weight=1000)
    tile = level.tile_grid[row][col]
    tile.add_thing(tree)
    tree.assign_sprite(sprite_file)
    tree.health = 130
    return tree


def GenerateBranch(level, row, col, sprite_file):
    branch = Thing(name='Branch', size=1, weight=10)
    tile = level.tile_grid[row][col]
    tile.add_thing(branch)
    branch.assign_sprite(sprite_file)
    return branch


def GenerateWolf(level, row, col, sprite_file):
    wolf = Agent(name='Wolf', size=2, weight=30, maxcapacity=200, health=50, cooldownmod=1)
    tile = level.tile_grid[row][col]
    tile.add_thing(wolf)
    wolf.assign_sprite(sprite_file)

    def ai(self):
        import random
        if self.cooldown == 0:
            directions = ['up', 'down', 'left', 'right']
            random_direction = random.choice(directions)
            self.move(random_direction, 30)

    wolf.ai = MethodType(ai, wolf)
    return wolf


def GenerateSquirrel(level, row, col, sprite_file):
    squirrel = Agent(name='Squirrel', size=1, weight=5, maxcapacity=20, health=10)
    tile = level.tile_grid[row][col]
    tile.add_thing(squirrel)
    squirrel.assign_sprite(sprite_file)
    return squirrel


def GenerateHermit(level, row, col, sprite_file):
    hermit = Agent(name='Hermit', size=1, weight=60, maxcapacity=400, health=80)
    tile = level.tile_grid[row][col]
    tile.add_thing(hermit)
    hermit.assign_sprite(sprite_file)
    return hermit

'''
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../graphics/weapons/rapier/full.png'},
}
'''