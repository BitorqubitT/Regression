import pygame
from operator import itemgetter

#TODO: Fix the convert function:
#Calculate the offset for where the graph starts
#Then calculate the position within the graph.

class Datapoints():
    def __init__(self, dataset, screen, offset, width, height):
        self.dataset = dataset
        self.screen = screen
        self.width = width - (width * 0.2)
        self.height = height - (height * 0.2)
        self.max_x = max(self.dataset, key=itemgetter(0))[0]
        self.max_y = max(self.dataset, key=itemgetter(1))[1]
        self.offset = offset

    def __convert_y(self, x, y):
        # We use plot-y = (height -  (y / ((max_plot_y) / (height ))))
        # We use plot-x = (x / ((max_plot_x) / (width )))
        # Pygame starts at 0 from top left we have to convert the y for visualisation.
        # We convert them to integers since pygame.draw wants integers
        x = int((x / ((self.max_x) / (self.width))) + self.offset)
        y = int((self.height - (y / ((self.max_y) / (self.height)))) + self.offset)
        return x, y

    def draw_data_points(self):
        # draw each datapoint
        # We use convert y so the visualisation matches the y values from the datapoints.
        for i in self.dataset:
            pygame.draw.circle(self.screen, (255, 0, 0),
                (self.__convert_y(i[0], i[1])[0], self.__convert_y(i[0], i[1])[1]),
                 1)

