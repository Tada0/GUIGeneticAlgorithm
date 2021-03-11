from random import random, sample


class Inversion:

    @staticmethod
    def get_method():
        return Inversion.__inversion

    @staticmethod
    def __inversion(population, probability):
        for chromosome in population.get_chromosomes():
            if random() < probability:
                bit1, bit2 = sorted(sample(range(1, len(chromosome.get_gene_x())-1), 2))
                gene_x = chromosome.get_gene_x()
                gene_y = chromosome.get_gene_y()
                chromosome.set_genes(
                    gene_x=gene_x[:bit1] + [int(not bit) for bit in gene_x[bit1:bit2]] + gene_x[bit2:],
                    gene_y=gene_y[:bit1] + [int(not bit) for bit in gene_y[bit1:bit2]] + gene_y[bit2:]
                )
