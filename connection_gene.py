

class Gene:
    def __init__(self, node_1, node_2, weight, inno_num):
        self.node_1 = node_1
        self.node_2 = node_2
        self.weight = weight
        self.enable = True
        self.inno_num = inno_num

    def clone(self):
        pass
