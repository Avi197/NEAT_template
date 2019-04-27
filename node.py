import numpy as np


class Node:
    def __init__(self, id_num):
        self.id_num = id_num
        self.in_sum = 0
        self.out_value = 0
        self.layer = 0

    def activate(self):
        self.out_value = 1/(1+np.exp(-4.9 * self.in_sum))

    def clone(self):
        pass

