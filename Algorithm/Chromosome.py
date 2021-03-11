from random import randint
from math import cos


class Chromosome:
    def __init__(self, gene_length, min_value, max_value):
        self.__min_value = min_value
        self.__max_value = max_value
        self.__gene_length = gene_length
        self.__gene_x = [randint(0, 1) for _ in range(gene_length)]
        self.__gene_y = [randint(0, 1) for _ in range(gene_length)]
        self.__fitness = None

    def __lt__(self, other):
        return self.get_fitness() < other.get_fitness()

    def __repr__(self):
        return f"Fitness: {self.__fitness} X: {self.__gene_x} Y: {self.__gene_y}"

    def set_genes(self, gene_x, gene_y):
        self.__gene_x = gene_x
        self.__gene_y = gene_y

    def get_fitness(self):
        return self.__fitness

    def get_gene_x(self):
        return self.__gene_x

    def get_gene_y(self):
        return self.__gene_y

    def get_gene_x_decimal(self):
        gene = "".join([str(bit) for bit in self.__gene_x])
        return self.__min_value + int(gene, 2) * (self.__max_value - self.__min_value) / (2 ** self.__gene_length - 1)

    def get_gene_y_decimal(self):
        gene = "".join([str(bit) for bit in self.__gene_y])
        return self.__min_value + int(gene, 2) * (self.__max_value - self.__min_value) / (2 ** self.__gene_length - 1)

    def calculate_fitness(self):
        self.__fitness = self.__calculate_function_value()

    def __calculate_function_value(self):
        numerator = 1 + cos(12 * (self.get_gene_x_decimal() ** 2 + self.get_gene_y_decimal() ** 2) ** 0.5)
        denominator = 0.5 * (self.get_gene_x_decimal() ** 2 + self.get_gene_y_decimal() ** 2) + 2
        return -1 * numerator / denominator
