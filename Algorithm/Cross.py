from copy import deepcopy
from random import random, randint, sample


class Cross:
    def __init__(self, cross_method):
        self.__cross_method = {
            'One Point': Cross.__one_point,
            'Two Points': Cross.__two_points,
            'Three Points': Cross.__three_points,
            'Homogenetic': Cross.__homo
        }[cross_method]

    def get_method(self):
        return self.__cross_method

    @staticmethod
    def __crossing(crossing_method, chromosomes_for_crossing, crossing_probability):
        def chunks(li, n):
            return [li[i:i + n] for i in range(0, len(li), n)]

        chromosomes_copy = [chromosome for chromosome in chromosomes_for_crossing]
        paired_chromosomes = chunks(chromosomes_copy, 2)
        crossed_chromosomes = []

        for pair in paired_chromosomes:
            chromosome1_copy, chromosome2_copy = [deepcopy(chromosome) for chromosome in pair]

            crossed_gene_x_1, crossed_gene_x_2 = crossing_method(
                gene1=chromosome1_copy.get_gene_x(),
                gene2=chromosome2_copy.get_gene_x(),
                probability=crossing_probability
            )

            crossed_gene_y_1, crossed_gene_y_2 = crossing_method(
                gene1=chromosome1_copy.get_gene_y(),
                gene2=chromosome2_copy.get_gene_y(),
                probability=crossing_probability
            )

            chromosome1_copy.set_genes(
                gene_x=crossed_gene_x_1,
                gene_y=crossed_gene_y_1
            )

            chromosome2_copy.set_genes(
                gene_x=crossed_gene_x_2,
                gene_y=crossed_gene_y_2
            )

            crossed_chromosomes.extend([chromosome1_copy, chromosome2_copy])

        return crossed_chromosomes

    @staticmethod
    def __one_point(chromosomes_for_crossing, crossing_probability):
        return Cross.__crossing(
            crossing_method=Cross.__one_point_crossing,
            chromosomes_for_crossing=chromosomes_for_crossing,
            crossing_probability=crossing_probability
        )

    @staticmethod
    def __two_points(chromosomes_for_crossing, crossing_probability):
        return Cross.__crossing(
            crossing_method=Cross.__two_points_crossing,
            chromosomes_for_crossing=chromosomes_for_crossing,
            crossing_probability=crossing_probability
        )

    @staticmethod
    def __three_points(chromosomes_for_crossing, crossing_probability):
        return Cross.__crossing(
            crossing_method=Cross.__three_points_crossing,
            chromosomes_for_crossing=chromosomes_for_crossing,
            crossing_probability=crossing_probability
        )

    @staticmethod
    def __homo(chromosomes_for_crossing, crossing_probability):
        return Cross.__crossing(
            crossing_method=Cross.__homo_crossing,
            chromosomes_for_crossing=chromosomes_for_crossing,
            crossing_probability=crossing_probability
        )

    @staticmethod
    def __one_point_crossing(gene1, gene2, probability):
        new_gene1, new_gene2 = gene1, gene2

        if random() < probability:
            cross_p = randint(1, len(new_gene1) - 1)
            gene1_part_1, gene1_part_2 = (
                new_gene1[:cross_p], new_gene1[cross_p:]
            )
            gene2_part_1, gene2_part_2 = (
                new_gene2[:cross_p], new_gene2[cross_p:]
            )
            new_gene1 = gene1_part_1 + gene2_part_2
            new_gene2 = gene2_part_1 + gene1_part_2

        return new_gene1, new_gene2

    @staticmethod
    def __two_points_crossing(gene1, gene2, probability):
        new_gene1, new_gene2 = gene1, gene2

        if random() < probability:
            cross_p1, cross_p2 = sorted(sample(range(1, len(new_gene1) - 1), 2))
            gene1_part_1, gene1_part_2, gene1_part_3 = (
                new_gene1[:cross_p1], new_gene1[cross_p1:cross_p2], new_gene1[cross_p2:]
            )
            gene2_part_1, gene2_part_2, gene2_part_3 = (
                new_gene2[:cross_p1], new_gene2[cross_p1:cross_p2], new_gene2[cross_p2:]
            )
            new_gene1 = gene1_part_1 + gene2_part_2 + gene1_part_3
            new_gene2 = gene2_part_1 + gene1_part_2 + gene2_part_3

        return new_gene1, new_gene2

    @staticmethod
    def __three_points_crossing(gene1, gene2, probability):
        new_gene1, new_gene2 = gene1, gene2

        if random() < probability:
            cross_p1, cross_p2, cross_p3 = sorted(sample(range(1, len(new_gene1) - 1), 3))
            gene1_part_1, gene1_part_2, gene1_part_3, gene1_part_4 = (
                new_gene1[:cross_p1], new_gene1[cross_p1:cross_p2], new_gene1[cross_p2:cross_p3], new_gene1[cross_p3:]
            )
            gene2_part_1, gene2_part_2, gene2_part_3, gene2_part_4 = (
                new_gene2[:cross_p1], new_gene2[cross_p1:cross_p2], new_gene2[cross_p2:cross_p3], new_gene2[cross_p3:]
            )
            new_gene1 = gene1_part_1 + gene2_part_2 + gene1_part_3 + gene2_part_4
            new_gene2 = gene2_part_1 + gene1_part_2 + gene2_part_3 + gene1_part_4

        return new_gene1, new_gene2

    @staticmethod
    def __homo_crossing(gene1, gene2, probability):
        new_gene1, new_gene2 = [], []
        for n in range(len(gene1)):
            if random() < probability:
                new_gene1.append(gene2[n])
                new_gene2.append(gene1[n])
            else:
                new_gene1.append(gene1[n])
                new_gene2.append(gene2[n])

        return new_gene1, new_gene2

