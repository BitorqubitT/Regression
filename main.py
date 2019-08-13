# Write the class that creates a graph in pygame.
# (give in: x_name, y_name, scale(this depends on the MAX and min value of the given data set.))
import random
import pygame
import Graph
import Datapoints
import Function

HEIGHT, WIDTH = 1000, 1000
AMOUNT_OF_DATAPOINTS = 100
MAX_SLOPE = 1.8
BEGIN_SLOPE = -1
CONSTANT_STEPS = 10
SLOPE_STEPS = 0.1
COLOUR = [255, 255, 255]
BLACK = [000, 000, 000]
X_NAME = "x"
Y_NAME = "y"
screen = pygame.display.set_mode((HEIGHT, WIDTH))


def generate_data_points(amount, width, height):
    i = 0
    datapoints = []
    while i != amount:
        #should change this for more range I should also consider creating a test data file for this
        datapoints.append((random.randint(200, width),random.randint(600, height)))
        i += 1
    return datapoints

def main():
    pygame.init()
    dataset = generate_data_points(AMOUNT_OF_DATAPOINTS, HEIGHT, WIDTH)
    running = True
    clock = pygame.time.Clock()
    datapoints = Datapoints.Datapoints(dataset, screen, AMOUNT_OF_DATAPOINTS, HEIGHT, WIDTH)
    graph = Graph.Graph(screen, BLACK, X_NAME, Y_NAME, HEIGHT, WIDTH)
    function = Function.Function(dataset, screen, HEIGHT, WIDTH, AMOUNT_OF_DATAPOINTS)

    while running:
        clock.tick(140)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = Falsescreen
        else:
            screen.fill(COLOUR)
            graph.draw()
            function.calculate_distance()
            function.slope += SLOPE_STEPS
            if function.slope >= MAX_SLOPE:
                function.constant += CONSTANT_STEPS
                function.slope = BEGIN_SLOPE
            if function.constant >= HEIGHT:
                print(function.optimal)
                function.slope = function.optimal[1]
                function.constant = function.optimal[2]
                function.draw_line()
                running = False
            datapoints.draw_data_points()
            function.draw_line()
            pygame.display.flip()

if __name__ == "__main__":
    main()
