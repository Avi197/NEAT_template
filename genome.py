from node import Node
from connection_gene import Gene
# from matrix import Matrix
from random import randrange


class Genome:
    def __init__(self, num_inputs, num_outputs):
        self.nodes = []  # dictionary so it can be in the right order?
        self.genes = []
        self.layers = 2
        self.layer_node = []
        self.next_node_id = 0
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs

        for i in range(num_inputs):
            self.nodes.append(Node(i))
            self.next_node_id += 1
            # self.nodes[i].layer = 0

        for i in range(num_outputs):
            self.nodes.append(Node(i + num_inputs))
            self.next_node_id += 1
            self.nodes[i + num_inputs].layer = 1

    def set_layer(self):
        for layer in range(self.layers):
            smt = []
            for n in self.nodes:
                if n.layer == layer:
                    smt.append(n)
            self.layer_node.append(smt)

    def feed_forward(self, inputs):
        results = []
        for i in range(len(inputs)):
            self.nodes[i].out_value = inputs[i]

        for layer in self.layer_node[1:]:
            for node in layer:
                for gene in self.genes:
                    if not gene.enable or node.id_num != gene.node_2.id_num:
                        continue
                    input_node = self.nodes[gene.node_1.id_num]
                    node.in_sum += gene.weight * input_node.out_value
                node.transmat_firing()

        for node in self.nodes[self.num_inputs:self.num_inputs+self.num_outputs]:
            results.append(node.out_value)

    def crossover(self, parent_2):
        parent_1 = self.genes

        pass

    def mutate(self):
        pass

    def add_node(self):
        chosen = int(randrange(len(self.genes)))  # select a random connection gene in genome and mutate
        self.genes[chosen].enable = False
        new_node_id = self.next_node_id
        self.nodes.append(Node(new_node_id))

        #
        inno_num = 0
        #

        new_connection_gene_1 = Gene(self.genes[chosen].node_1, self.nodes[new_node_id], 1, inno_num)
        new_connection_gene_2 = Gene(self.nodes[new_node_id], self.genes[chosen].node_2,
                                     self.genes[chosen].weight, inno_num)

        # set layer for new node
        self.nodes[new_node_id].layer = self.genes[chosen].node_1.layer + 1

        # if new node layer == old_2 node layer, add a new layer
        if self.nodes[new_node_id].layer == self.genes[chosen].node_2.layer:
            # except the last one, cause we just add that last one
            for i in self.nodes[:-1]:
                if i.layer >= self.nodes[new_node_id].layer:
                    i.layer += 1
            self.layers += 1

        self.genes.append(new_connection_gene_1)
        self.genes.append(new_connection_gene_2)

    def add_connection(self):

        random_node_1 = int(randrange(0, len(self.nodes)))
        random_node_2 = int(randrange(0, len(self.nodes)))
        # print(random_node_1)
        # print(random_node_2)
        while self.cant_connect(random_node_1, random_node_2):
            random_node_1 = int(randrange(0, len(self.nodes)))
            random_node_2 = int(randrange(0, len(self.nodes)))
            # print(random_node_1)
            # print(random_node_2)

        # reverse the connection of 2 node if layers are reverse
        if self.nodes[random_node_1].layer > self.nodes[random_node_2].layer:
            random_node_1, random_node_2 = random_node_2, random_node_1

        #
        inno_num = 0  # need to implement innonum here
        weight = 1  # this too
        #
        connection_gene = Gene(self.nodes[random_node_1], self.nodes[random_node_2], weight, inno_num)
        self.genes.append(connection_gene)

    def cant_connect(self, n1, n2):

        if self.nodes[n1].layer == self.nodes[n2].layer:
            return True

        for i in self.genes:
            if self.nodes[n1] == i.node_1 and self.nodes[n2] == i.node_2:
                return True
            if self.nodes[n2] == i.node_1 and self.nodes[n1] == i.node_2:
                return True

    # def neu_net(self):
    #     for i in

    # def test(self, nodes_in_layer):
    #     m = Matrix(len(nodes_in_layer), 1)
    #     for i in len(nodes_in_layer):
    #         m.data[i][0] = nodes_in_layer[i]
    #     return m

    # def feed_forward(self):


# a = Matrix(3, 3)
# print(a.data)
a = Genome(3, 2)
