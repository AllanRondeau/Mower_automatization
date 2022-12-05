class Mower:
    # constructor for mower class, define point object to contain coords,
    # direction attributes to contain the cardinal direction of the mower.
    def __init__(self, point, direction):
        self.point = point
        self.arr_instruction = None
        self.direction = direction

    # Set new points for the mower
    def set_point_x(self, point_x):
        self.point.set_x(point_x)

    def set_point_y(self, point_y):
        self.point.set_y(point_y)

    def set_direction(self, direction):
        self.direction = direction

    # set an array to contain instruction

    def set_instruction(self, arr_instruction):
        self.arr_instruction = arr_instruction

        # methods to get Mower attributes

    def get_point_x(self):
        return self.point.get_x()

    def get_point_y(self):
        return self.point.get_y()

    def get_instruction(self):
        return self.arr_instruction

    def get_direction(self):
        return self.direction

    # method to return the final coord of the Mower when it has finish his task.

    def create_point_with_card_dir(self):
        position = str(self.point.get_x()) + str(self.point.get_y()) + self.direction
        return position
