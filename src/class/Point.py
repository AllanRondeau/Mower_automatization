class Point:
    # Class point to create geometric coords. x for abscissa and y for ordinate.
    def __init__(self, abs, ord):
        self.x = abs
        self.y = ord
    # method to set x and y

    def set_x(self, dx):
        self.x = dx
        return self.x

    def set_y(self, dy):
        self.y = dy
        return self.y
    # method to get x and y values

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
