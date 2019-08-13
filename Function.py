import math
import pygame
import random
from operator import itemgetter

class Function():
    def __init__(self, dataset, screen, width, height, offset):
        # We begin with a certain slope and constant before iterating.
        self.dataset = dataset
        self.optimal = [100000000, 0, 0]
        self.slope = -1
        self.constant = 1
        self.screen = screen
        self.width = width - (width * 0.2)
        self.height = height - (height * 0.2)
        self.offset = offset
        self.max_x = max(self.dataset, key=itemgetter(0))[0]
        self.max_y = max(self.dataset, key=itemgetter(1))[1]

# Functions below are for visualising.
# We have to convert here aswell to draw the line.
# We start IN THE GRAPH and the line stops at the edge of the graph.
    def __convert_y(self, x, y):
        # We use plot-y = (height -  (y / ((max_plot_y) / (height ))))
        # We use plot-x = (x / ((max_plot_x) / (width )))
        # Pygame starts at 0 from top left we have to convert the y for visualisation.
        # We convert them to integers since pygame.draw wants integers
        x = int((x / ((self.max_x) / (self.width))) + self.offset)
        y = int((self.height - (y / ((self.max_y) / (self.height)))) + self.offset)
        return x, y

    def draw_line(self):
        # y = mx + b
        x_end = 800
        x_begin = 0
        end = self.slope * x_end + self.constant
        pygame.draw.line(self.screen, (255, 0, 0), (self.__convert_y(x_begin, self.constant)[0], self.__convert_y(x_begin, self.constant)[1]), (self.height + self.offset, self.__convert_y(self.constant, end)[1]), 1)
        # just draw a line with a certain incline.
        # Use the inputs to draw the line.
        # This function will keep being updated.

# Functions below are for actual calculating.
    def calculate_distance(self):
        distance_total = 0
        # Here we calculate the distance between each point and the line.
        # The coordinates of closest point on the line is.
        # x = (b(bx_0 - ay_0) - ac) / (a^2 + b ^2 )
        # y = (a(-bx_0 + ay_0) - bc)/ (a ^2 + b^2)
        # The a and b cannot be zero
        a = self.slope
        b = -1
        c = self.constant
        # HAVE TO CHECK THE B-1 by testing it with just 1 point and findint the optimal line.
        # Than calculate it by hand
        for i in self.dataset:
            x = (b * (b * i[0] - a * i[1]) - a * c) / (a ** 2 + b ** 2)
            y = (a * (-b * i[0] + a * i[1]) - b * c) / (a ** 2 + b ** 2)
            # calculate distance
            # D = sqrt((x_2 - X_1) ^ 2 + (y_2 - y_1) ^ 2)
            distance = math.sqrt(((i[0] - x) ** 2) + ((i[1] - y) ** 2))
            distance_total = distance_total + distance
        #self.new_record_distance = distance_total, a , c
        if distance_total < self.optimal[0]:
            self.optimal[0] = distance_total
            self.optimal[1] = a
            self.optimal[2] = c
        return distance_total, a, c


        # y=mx+b
        # y = self.slope * i[0] + self.constant
        # distance = y - i[1]




