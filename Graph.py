import pygame

class Graph():
    def __init__(self, screen, colour, label_x, label_y, height, width):
        self.label_x = label_x
        self.label_y = label_y
        self.colour = colour
        self.screen = screen
        self.height = height
        self.width = width


    def draw(self):
        # X
        # Set font we have to do this.
        x_start, y_start = self.width * 0.1, self.height * 0.9
        x_end, y_end = self.width * 0.9, self.height * 0.1
        font = pygame.font.SysFont("comicsansms", 12)
        # name, colour
        text_x = font.render(self.label_x, True, (133, 128, 0))
        text_y = font.render(self.label_y, True, (133, 128, 0))
        self.screen.blit(text_x,(self.width - 100, self.height - 100))
        self.screen.blit(text_y,(self.width - 920, self.height - 900))

        pygame.draw.line(self.screen, self.colour, (x_start, y_start), (x_end, y_start))
        pygame.draw.line(self.screen, self.colour, (x_start, y_start), (x_start, y_end))



