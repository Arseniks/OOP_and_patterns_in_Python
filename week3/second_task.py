class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        lights = []
        obstacles = []
        for height, line in enumerate(grid):
            for width, elem in enumerate(line):
                if elem == 1:
                    lights.append((width, height))
                elif elem == -1:
                    obstacles.append((width, height))
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()

