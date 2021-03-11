from random import random, randint, sample


class Mutation:
    def __init__(self, mutation_method):
        self.__mutation_method = {
            'Edge': Mutation.__edge,
            'One Point': Mutation.__one_point,
            'Two Points': Mutation.__two_points
        }[mutation_method]

    def get_method(self):
        return self.__mutation_method

    @staticmethod
    def __edge(population, probability):
        for chromosome in population.get_chromosomes():
            if random() < probability:
                chromosome.set_genes(
                    gene_x=chromosome.get_gene_x()[:-1] + [int(not (chromosome.get_gene_x()[-1]))],
                    gene_y=chromosome.get_gene_y()[:-1] + [int(not (chromosome.get_gene_y()[-1]))]
                )

    @staticmethod
    def __one_point(population, probability):
        for chromosome in population.get_chromosomes():
            if random() < probability:
                bit = randint(0, len(chromosome.get_gene_x()) - 1)
                gene_x = chromosome.get_gene_x()
                gene_y = chromosome.get_gene_y()
                chromosome.set_genes(
                    gene_x=gene_x[:bit] + [int(not gene_x[bit])] + gene_x[bit + 1:],
                    gene_y=gene_y[:bit] + [int(not gene_y[bit])] + gene_y[bit + 1:],
                )

    @staticmethod
    def __two_points(population, probability):
        for chromosome in population.get_chromosomes():
            if random() < probability:
                for bit in sample(range(0, len(chromosome.get_gene_x())), 2):
                    gene_x = chromosome.get_gene_x()
                    gene_y = chromosome.get_gene_y()
                    chromosome.set_genes(
                        gene_x=gene_x[:bit] + [int(not gene_x[bit])] + gene_x[bit+1:],
                        gene_y=gene_y[:bit] + [int(not gene_y[bit])] + gene_y[bit+1:],
                    )
