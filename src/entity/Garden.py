class Garden:

    def __init__(self, point):
        self.point = point

    def get_point_x(self):
        return self.point.get_x()

    def get_point_y(self):
        return self.point.get_y()

    def set_point_x(self, point_x):
        self.point.set_x(self, point_x)

    def set_point_y(self, point_y):
        return self.point.set_y(self, point_y)
