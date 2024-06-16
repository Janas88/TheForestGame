import pygame
from settings import TILESIZE, TILE_INTERPRETATION, WORLD_MAP, POPULATE_MAP, WIDTH, HEIGHT
from Tile.Tile import Tile
from thing.agent.Agentmod import Agent

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.tile_grid = []
        self.thing_sprites = pygame.sprite.Group()
        self.camera_offset_x = 0
        self.camera_offset_y = 0

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            tile_row = []
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                surface = TILE_INTERPRETATION.get(col, 'grass')
                tile = Tile([row_index, col_index], self, surface)
                self.visible_sprites.add(tile)
                tile_row.append(tile)
            self.tile_grid.append(tile_row) #a tutaj costam innego

        for row, line in enumerate(POPULATE_MAP):
            for col, char in enumerate(line):
                if char in TILE_INTERPRETATION:
                    populate = TILE_INTERPRETATION[char]
                    if callable(populate):
                        populate(self, row, col)

    def render_things(self, display_surface):
        self.thing_sprites.empty()  # Clear the thing sprites group

        player_tile = None  # Initialize player_tile variable

        for row_index, row in enumerate(self.tile_grid):
            for col_index, tile in enumerate(row):
                if tile.has_player():
                    player_tile = tile  # Save player's tile reference for later use

                tile_x = col_index * TILESIZE + self.camera_offset_x
                tile_y = row_index * TILESIZE + self.camera_offset_y
                display_surface.blit(tile.image, (tile_x, tile_y))

        if player_tile is not None:
            player_pos = player_tile.pos
            self.camera_offset_x = WIDTH // 2 - player_pos[1] * TILESIZE - TILESIZE // 2
            self.camera_offset_y = HEIGHT // 2 - player_pos[0] * TILESIZE - TILESIZE // 2

        for row_index, row in enumerate(self.tile_grid):
            for col_index, tile in enumerate(row):
                thinglist = tile.get_contents()
                for thing in thinglist:
                    thing_sprite = thing.get_sprite()

                    if thing_sprite is not None:
                        thing_sprite.rect.topleft = (
                            col_index * TILESIZE + self.camera_offset_x,
                            row_index * TILESIZE + self.camera_offset_y
                        )
                        self.thing_sprites.add(thing_sprite)  # Add the thing's sprite to the group

        self.thing_sprites.draw(self.display_surface)

    def handle_events(self):
        for row_index, row in enumerate(self.tile_grid):
            for col_index, tile in enumerate(row):
                thinglist = tile.get_contents()
                for agent in thinglist:
                    if isinstance(agent, Agent):
                        agent.update_cooldown()
                        agent.input()

    def get_tile_at_position(self, position):
        row_index, col_index = position
        if (
            0 <= row_index < len(self.tile_grid) and
            0 <= col_index < len(self.tile_grid[row_index])
        ):
            return self.tile_grid[row_index][col_index]
        else:
            return None

    def show_attack(self):
        pass
#zmieniam cos tutaj
    def run(self):
        self.visible_sprites.update()
        self.visible_sprites.draw(self.display_surface)
#Level rework costam