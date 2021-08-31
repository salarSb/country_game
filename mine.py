import math

from work_place import WorkPlace, Consts


class Mine(WorkPlace):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.expertise = 'mine'

    def calc_capacity(self):
        self.capacity = math.pow(self.level, 2)

    def calc_costs(self):
        costs = Consts.BASE_PLACE_COST + (Consts.LEVEL_MUL * self.level)
        return costs
