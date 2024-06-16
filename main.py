import pygame
import sys
from io import StringIO
from settings import *
from Level import Level
import pygame.font

sys.stdout = StringIO()
font_path = FONT_PATH #cośtam cośtam
font_size = CONSOLE_FONT_SIZE #branchout


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('The Forest')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.level.create_map()
        self.console_surface = pygame.Surface((CONSOLE_WIDTH, CONSOLE_HEIGHT))
        pygame.font.init()
        self.console_font = pygame.font.Font(FONT_PATH, CONSOLE_FONT_SIZE)
        self.player = None

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.run()

            self.screen.fill(pygame.Color('black'))
            self.level.render_things(self.screen)
            self.level.handle_events()

            self.render_console()

            pygame.display.flip()
            self.clock.tick(FPS)

    def render_console(self):
        self.console_surface.fill(CONSOLE_BG_COLOR)

        # Get the latest console prints and split them by newline
        console_prints = sys.stdout.getvalue().split('\n')
        num_lines = min(CONSOLE_HEIGHT // CONSOLE_FONT_SIZE, len(console_prints))

        # Render each line of console prints on the console surface
        for i in range(num_lines):
            line = console_prints[-num_lines + i]
            text_surface = self.console_font.render(line, True, CONSOLE_FONT_COLOR)
            self.console_surface.blit(text_surface, (0, i * CONSOLE_FONT_SIZE))

        # Blit the console surface onto the main screen
        self.screen.blit(self.console_surface, (0, HEIGHT - CONSOLE_HEIGHT))


if __name__ == '__main__':
    game = Game()
    game.run()
