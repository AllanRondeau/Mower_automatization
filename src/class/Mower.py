class Mower:
    # constructor for mower class, define point object to contain coords, array for instruction,
    # direction attributes to contain the cardinal direction of the mower.
    def __init__(self, point, arrInstruction, direction):
        self.point = point
        self.arrInstruction = arrInstruction
        self.direction = direction

    # Set new points for the mower
    def set_pointx(self, pointx):
        return self.point.set_x(self, pointx)

    def set_pointy(self, pointy):
        return self.point.set_y(self, pointy)

